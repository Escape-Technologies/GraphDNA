"""Manage heuristics flow."""

import logging
from typing import Optional

from graphdna.entities.engines import GraphQLEngine
from graphdna.entities.interfaces.dna import IHTTPBucket
from graphdna.entities.interfaces.heuristics import IHeuristicsManager
from graphdna.heuristics.gql_queries import GQLQueriesManager
from graphdna.heuristics.web_properties import WebPropertiesManager


class HeuristicsManager(IHeuristicsManager):

    def __init__(
        self,
        logger: logging.Logger,
    ) -> None:
        self._logger = logger
        self._candidates = {}

        self._gql_queries_manager = GQLQueriesManager(self._logger)
        self._web_properties_manager = WebPropertiesManager(self._logger)

    def load(self) -> None:
        self._gql_queries_manager.load()
        self._web_properties_manager.load()

    async def enqueue_requests(
        self,
        bucket: IHTTPBucket,
    ) -> None:
        await self._gql_queries_manager.enqueue_requests(bucket)
        await self._web_properties_manager.enqueue_requests(bucket)

    async def parse_requests(
        self,
        bucket: IHTTPBucket,
    ) -> None:
        async for match, engine in self._gql_queries_manager.parse_requests(bucket):
            self.add_score(match, engine)
        async for match, engine in self._web_properties_manager.parse_requests(bucket):
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
            self._logger.debug(f'{engine.name.capitalize()}: {round(score, 2)} pts')

    @property
    def best_candidate(self) -> Optional[GraphQLEngine]:
        """Fetch the best candidate engine.

        If any, the highest confidence will be returned.
        """

        sorted_candidates = sorted(
            self._candidates,
            reverse=True,
            key=lambda x: self._candidates[x],
        )
        candidate = sorted_candidates[0] if self._candidates else None
        candidate_literal = candidate.value if candidate else 'None, are you sure this is a GraphQL endpoint?'
        self._logger.info(f'Best candidate: {candidate_literal}')

        return candidate
