import asyncio
import logging
from typing import AsyncGenerator, Dict, List, Tuple

import aiohttp

from graphdna.entities.engines import GraphQLEngine
from graphdna.entities.interfaces.dna import IHTTPBucket, IRequest
from graphdna.entities.interfaces.heuristics import EvalMethods, IGQLQueriesManager, IGQLQuery
from graphdna.heuristics.utils import find_engine, import_heuristics


class GQLQueriesManager(IGQLQueriesManager):

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

        heuristics: List[IGQLQuery] = []
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
        # Refactor enqueue with a generator
        for heuristic in self._heuristics:
            new_genetics: Dict[str, EvalMethods] = {}

            for query, _evals in heuristic.genetics.items():
                req = IRequest('%%url%%', 'POST', {
                    'json': {
                        'query': query,
                    },
                    'headers': {
                        'Content-Type': 'application/json',
                    },
                })
                req_hash = await bucket.put(req)
                new_genetics[req_hash] = _evals

            heuristic.genetics = new_genetics

    async def parse_requests(  # type: ignore[override]
        self,
        bucket: IHTTPBucket,
    ) -> AsyncGenerator[Tuple[IGQLQuery, GraphQLEngine], None]:
        for heuristic in self._heuristics:
            for req_hash, _evals in heuristic.genetics.items():
                client_response = bucket.get(req_hash)
                if not client_response:
                    continue

                if not isinstance(_evals, List):
                    _evals = [_evals]

                for _eval in _evals:
                    try:
                        if not await _eval(client_response):
                            continue
                    except (aiohttp.client_exceptions.ContentTypeError, asyncio.TimeoutError):
                        self._logger.error('Response content unpacking failed.')
                        continue

                    yield heuristic, heuristic.__engine__
