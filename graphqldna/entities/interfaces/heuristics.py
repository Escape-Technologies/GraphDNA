# pylint: disable=missing-function-docstring,missing-class-docstring, too-few-public-methods

"""Manage the heuristics interfaces."""

import logging
from abc import ABC, abstractmethod
from typing import Callable

from graphqldna.entities.engines import GraphQLEngine
from graphqldna.entities.interfaces import IHTTPBucket
from graphqldna.entities.interfaces.dna import IRequest


class IHeuristic(ABC):

    _score: int
    _score_factor: int

    def verify(self) -> bool:
        raise NotImplementedError


class IGQLQuery(IHeuristic):

    _score_factor = 1
    genetic_correlation: dict[str, Callable]


class IAppProperties(IHeuristic):

    _score_factor = 1.2


class IHeuristicsManager(ABC):

    _logger: logging.Logger
    _candidates: dict[int, GraphQLEngine]

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    def gather_requests(self, url: str) -> list[IRequest]:
        ...

    @abstractmethod
    def parse_requests(self, bucket: IHTTPBucket) -> None:
        ...

    @abstractmethod
    def display_results(self) -> None:
        ...

    @property
    @abstractmethod
    def best_candidate(self) -> GraphQLEngine | None:
        ...
