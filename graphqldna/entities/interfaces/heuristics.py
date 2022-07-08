# pylint: disable=missing-function-docstring,missing-class-docstring, too-few-public-methods

"""Manage the heuristics interfaces."""

import logging
from abc import ABC, abstractmethod
from typing import Callable

from graphqldna.entities.engines import GraphQLEngine
from graphqldna.entities.interfaces import IHTTPBucket


class IHeuristic(ABC):

    score: int = 100
    score_factor: int = 1

    def verify(self) -> bool:
        raise NotImplementedError


class IGQLQuery(IHeuristic):

    genetic_correlation: dict[str, Callable]


class IAppProperties(IHeuristic):

    score_factor = 1.2


class IHeuristicsManager(ABC):

    _logger: logging.Logger
    _candidates: dict[int, GraphQLEngine]

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    async def enqueue_requests(self, url: str, bucket: IHTTPBucket) -> None:
        ...

    @abstractmethod
    async def parse_requests(self, bucket: IHTTPBucket) -> None:
        ...

    @abstractmethod
    def display_results(self) -> None:
        ...

    @property
    @abstractmethod
    def best_candidate(self) -> GraphQLEngine | None:
        ...