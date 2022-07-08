"""Manage heuristics flow."""

import logging

from graphqldna.entities.engines import GraphQLEngine
from graphqldna.entities.interfaces.dna import IHTTPBucket, IRequest
from graphqldna.entities.interfaces.heuristics import IHeuristicsManager
from graphqldna.heuristics.gql_queries import import_gql_queries


class HeuristicsManager(IHeuristicsManager):

    def __init__(self, logger: logging.Logger) -> None:

        self._logger = logger
        self._candidates = {}
        self._queries_heuristics = []

    def load(self) -> None:
        self._queries_heuristics = import_gql_queries()

    async def enqueue_requests(self, url: str, bucket: IHTTPBucket) -> None:
        requests: list[IRequest] = []

        for query_heuristic in self._queries_heuristics:

            new_correlation = {}

            for key, value in query_heuristic.genetic_correlation.items():
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

            query_heuristic.genetic_correlation = new_correlation

        return requests

    async def parse_requests(self, bucket: IHTTPBucket) -> None:
        for query_heuristic in self._queries_heuristics:
            for key, detector in query_heuristic.genetic_correlation.items():
                if await detector(bucket.get(key)):

                    self.add_score(query_heuristic.__engine__, query_heuristic)

    def add_score(self, engine: GraphQLEngine, cls: object) -> None:
        if engine not in self._candidates:
            self._candidates[engine] = 0

        self._candidates[engine] += cls.score * cls.score_factor

    def display_results(self) -> None:
        self._logger.debug('Heuristics results:')
        for engine, score in self._candidates.items():
            self._logger.debug(f'{engine.name.capitalize()}: {score} pts')

    @property
    def best_candidate(self) -> GraphQLEngine | None:
        """Fetch the best candidate engine.

        If any, the highest confidence will be returned.
        """

        candidate = sorted(self._candidates)[-1].value if self._candidates else None

        self._logger.info(f'Best candidate: \x1b[31;20m{candidate}\x1b[0m')
        return candidate
