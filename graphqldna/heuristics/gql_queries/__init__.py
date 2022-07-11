import logging
from typing import AsyncGenerator

import aiohttp

from graphqldna.entities.engines import GraphQLEngine
from graphqldna.entities.interfaces.dna import IHTTPBucket, IRequest
from graphqldna.entities.interfaces.heuristics import IGQLQueriesManager, IGQLQuery
from graphqldna.heuristics.utils import import_heuristics


def find_engine(
    engine: str,
    possibilities: list[str],
) -> str:
    for p in possibilities:
        if engine == p.lower():
            return p
    raise ValueError(f'Unknown engine `{engine}`, possibilities: {possibilities}')


class GQLQueriesManager(IGQLQueriesManager):

    def __init__(
        self,
        logger: logging.Logger,
    ) -> None:
        self._heuristics = []
        self._logger = logger

    async def enqueue_requests(
        self,
        url: str,
        bucket: IHTTPBucket,
    ) -> None:
        # Refactor enqueue with a generator
        for heuristic in self._heuristics:
            new_correlation = {}

            for key, value in heuristic.genetics.items():
                req = IRequest(url, 'POST', {
                    'json': {
                        'query': key,
                    },
                    'headers': {
                        'Content-Type': 'application/json',
                    },
                })
                req_hash = bucket.hash(req)
                await bucket.put(req, req_hash)

                new_correlation[req_hash] = value
            heuristic.genetics = new_correlation

    def load(self) -> None:
        raw_heuritics = import_heuristics(
            __file__,
            __name__,
        )

        heuristics: list[IGQLQuery] = []
        for raw in raw_heuritics:
            engine = raw.__name__.split('.')[-1]
            engine = find_engine(engine, dir(raw))

            cls = eval(f'raw.{engine}')  # pylint: disable=eval-used
            cls.__engine__ = GraphQLEngine(engine)
            heuristics.append(cls)

        self._heuristics = heuristics

    async def parse_requests(  # type: ignore[override]
        self,
        bucket: IHTTPBucket,
    ) -> AsyncGenerator[tuple[IGQLQuery, GraphQLEngine], None]:
        for heuristic in self._heuristics:
            for key, detectors in heuristic.genetics.items():
                client_response = bucket.get(key)

                if not isinstance(detectors, list):
                    detectors = [detectors]

                for detector in detectors:
                    try:
                        if not await detector(client_response):
                            continue
                    except aiohttp.client_exceptions.ContentTypeError:
                        self._logger.error('Response is not JSON. Are you sure this is a GraphQL endpoint?')
                        continue

                    yield heuristic, heuristic.__engine__
