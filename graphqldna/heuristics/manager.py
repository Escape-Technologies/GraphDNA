"""Manage heuristics flow."""

import logging

from graphqldna.entities.engines import GraphQLEngine
from graphqldna.entities.interfaces.dna import IHTTPBucket, IRequest
from graphqldna.entities.interfaces.heuristics import IHeuristicsManager
from graphqldna.heuristics.gql_queries import import_gql_queries


class HeuristicsManager(IHeuristicsManager):

    def __init__(self) -> None:
        """Init heuristics manager."""

        self._candidates = {}

    @property
    def best_candidate(self) -> GraphQLEngine | None:
        """Fetch the best candidate engine.

        If any, the highest confidence will be returned.
        """

        candidate = self._candidates[sorted(self._candidates)[-1]] if self._candidates else None

        self._logger.debug(f'Best candidate: \x1b[31;20m{candidate}\x1b[0m')
        return candidate
