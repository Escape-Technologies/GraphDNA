import asyncio
import logging
from typing import AsyncGenerator, List, Tuple, cast

import aiohttp

from graphdna.entities.engines import GraphQLEngine
from graphdna.entities.interfaces.dna import IHTTPBucket
from graphdna.entities.interfaces.heuristics import EvalMethods, IWebPropertiesManager, IWebProperty
from graphdna.heuristics.utils import find_engine, import_heuristics


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

        heuristics: List[IWebProperty] = []
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

            new_requests: List[Tuple[str, EvalMethods]] = []
            for req, _evals in heuristic.requests:
                req_hash = await bucket.put(req)

                new_requests.append((req_hash, _evals))

            heuristic.requests = new_requests  # type: ignore[assignment]

    async def parse_requests(  # type: ignore[override]
        self,
        bucket: IHTTPBucket,
    ) -> AsyncGenerator[Tuple[IWebProperty, GraphQLEngine], None]:

        for heuristic in self._heuristics:
            for req_hash, _evals in heuristic.requests:
                client_reponse = bucket.get(cast(str, req_hash))
                if not client_reponse:
                    continue

                if not isinstance(_evals, List):
                    _evals = [_evals]

                for _eval in _evals:
                    try:
                        if not await _eval(client_reponse):
                            continue
                    except (aiohttp.client_exceptions.ContentTypeError, asyncio.TimeoutError):
                        self._logger.error('Response content unpacking failed.')
                        continue

                    yield heuristic, heuristic.__engine__
