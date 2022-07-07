# pylint: disable=missing-function-docstring,missing-class-docstring, too-few-public-methods

"""Manage the heuristics interfaces."""

from abc import ABC, abstractmethod
from typing import Callable

from graphqldna.entities.engines import GraphQLEngine


class IHeuristic(ABC):

    _score: int
    _score_factor: int

    @abstractmethod
    def verify(self) -> bool:
        ...


class IGQLQuery(IHeuristic):

    _score_factor = 1
    _genetic_correlation: dict[str, Callable]


class IAppProperties(IHeuristic):

    _score_factor = 1.2


class IHeuristicsManager(ABC):

    _candidates: dict[int, GraphQLEngine]

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    def gather_requests(self) -> None:
        ...

    @abstractmethod
    def parse_requests(self) -> None:
        ...

    @abstractmethod
    def display_results(self) -> None:
        ...

    @property
    @abstractmethod
    def best_candidate(self) -> GraphQLEngine | None:
        ...
