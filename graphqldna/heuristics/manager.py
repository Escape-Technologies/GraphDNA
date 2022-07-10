"""Manage heuristics flow."""

import logging

from graphqldna.entities.engines import GraphQLEngine
from graphqldna.entities.interfaces.dna import IHTTPBucket
from graphqldna.entities.interfaces.heuristics import IHeuristicsManager
from graphqldna.heuristics.gql_queries import GQLQueriesManager


class HeuristicsManager(IHeuristicsManager):

    def __init__(
        self,
        logger: logging.Logger,
    ) -> None:
        self._logger = logger
        self._candidates = {}

        self._gql_queries_manager = GQLQueriesManager()

    def load(self) -> None:
        self._gql_queries_manager.load()

    async def enqueue_requests(
        self,
        url: str,
        bucket: IHTTPBucket,
    ) -> None:
        await self._gql_queries_manager.enqueue_requests(url, bucket)

    async def parse_requests(
        self,
        bucket: IHTTPBucket,
    ) -> None:
        async for match, engine in self._gql_queries_manager.parse_requests(bucket):
            self.add_score(match, engine)

    def add_score(
        self,
        cls: object,
        engine: GraphQLEngine,
    ) -> None:
        if engine not in self._candidates:
            self._candidates[engine] = 0

        self._candidates[engine] += cls.score * cls.score_factor

    def display_results(self) -> None:
        self._logger.debug('Pushing heuristics results...')

        for engine, score in self._candidates.items():
            self._logger.debug(f'{engine.name.capitalize()}: {score} pts')

    @property
    def best_candidate(self) -> GraphQLEngine | None:
        """Fetch the best candidate engine.

        If any, the highest confidence will be returned.
        """

        sorted_candidates = sorted(
            self._candidates,
            reverse=True,
            key=lambda x: self._candidates[x],
        )
        candidate = sorted_candidates[0] if self._candidates else None

        self._logger.info(f'Best candidate: {candidate.value if candidate else "None"}')
        return candidate
