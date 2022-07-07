"""Manage heuristics flow."""

from graphqldna.entities.engines import GraphQLEngine
from graphqldna.entities.interfaces.dna import IHTTPBucket
from graphqldna.entities.interfaces.heuristics import IHeuristicsManager


class HeuristicsManager(IHeuristicsManager):

    def __init__(self) -> None:
        """Init heuristics manager."""

        self._candidates = {}

    @property
    def best_candidate(self) -> GraphQLEngine | None:
        """Fetch the best candidate engine.

        If any, the highest confidence will be returned.
        """

        return self._candidates[sorted(self._candidates)[-1]] if self._candidates else None
