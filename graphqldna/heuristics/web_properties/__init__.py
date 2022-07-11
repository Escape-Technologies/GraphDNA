import logging
from typing import AsyncGenerator, cast

import aiohttp

from graphqldna.entities.engines import GraphQLEngine
from graphqldna.entities.interfaces.dna import IHTTPBucket, IRequest
from graphqldna.entities.interfaces.heuristics import EvalMethods, IWebPropertiesManager, IWebProperty
from graphqldna.heuristics.utils import find_engine, import_heuristics


class WebPropertiesManager(IWebPropertiesManager):

    def __init__(
        self,
        logger: logging.Logger,
    ) -> None:
        self._heuristics = []

        self._logger = logger

    def load(self) -> None:
        raw_heuritics = import_heuristics(
            __file__,
            __name__,
        )

        heuristics: list[IWebProperty] = []
        for raw in raw_heuritics:
            engine = raw.__name__.split('.')[-1]
            engine = find_engine(engine, dir(raw))

            cls = eval(f'raw.{engine}')  # pylint: disable=eval-used
            cls.__engine__ = GraphQLEngine(engine)
            heuristics.append(cls)

        self._heuristics = heuristics

    async def enqueue_requests(
        self,
        bucket: IHTTPBucket,
    ) -> None:
        for heuristic in self._heuristics:

            new_requests: list[tuple[str, EvalMethods]] = []
            for req, _evals in heuristic.requests:
                req_hash = await bucket.put(req)

                new_requests.append((req_hash, _evals))

            heuristic.requests = new_requests  # type: ignore[assignment]

    async def parse_requests(  # type: ignore[override]
        self,
        bucket: IHTTPBucket,
    ) -> AsyncGenerator[tuple[IWebProperty, GraphQLEngine], None]:

        for heuristic in self._heuristics:
            for req_hash, _evals in heuristic.requests:
                client_reponse = bucket.get(cast(str, req_hash))

                if not isinstance(_evals, list):
                    _evals = [_evals]

                for _eval in _evals:
                    try:
                        if not await _eval(client_reponse):
                            continue
                    except aiohttp.client_exceptions.ContentTypeError:
                        continue

                    yield heuristic, heuristic.__engine__
