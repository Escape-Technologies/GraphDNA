"""Manage the heuristics interfaces."""

import functools
import logging
from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator

from graphqldna.entities.engines import GraphQLEngine
from graphqldna.entities.interfaces import IHTTPBucket
from graphqldna.entities.interfaces.dna import IRequest


class IHeuristic(ABC):

    score: int = 100
    score_factor: float = 1.0

    def verify(self) -> bool:
        raise NotImplementedError


class IGQLQuery(IHeuristic):

    genetics: dict[str, functools.partial | list[functools.partial]]


class IWebProperty(IHeuristic):

    requests: list[IRequest]


class IAppProperties(IHeuristic):

    score_factor = 1.2


class IHeuristicManager(ABC):

    @abstractmethod
    async def enqueue_requests(
        self,
        url: str,
        bucket: IHTTPBucket,
    ) -> None:
        ...

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    async def parse_requests(
        self,
        bucket: IHTTPBucket,
    ) -> AsyncGenerator[Any, None]:
        ...


class IGQLQueriesManager(IHeuristicManager):

    _heuristics: list[IGQLQuery]


class IWebPropertiesManager(IHeuristicManager):

    ...


class IHeuristicsManager(ABC):

    _logger: logging.Logger
    _candidates: dict[GraphQLEngine, int]

    _gql_queries_manager: IHeuristicManager

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    async def enqueue_requests(
        self,
        url: str,
        bucket: IHTTPBucket,
    ) -> None:
        ...

    @abstractmethod
    async def parse_requests(
        self,
        bucket: IHTTPBucket,
    ) -> None:
        ...

    @abstractmethod
    def add_score(
        self,
        cls: object,
        engine: GraphQLEngine,
    ) -> None:
        ...

    @abstractmethod
    def display_results(self) -> None:
        ...

    @property
    @abstractmethod
    def best_candidate(self) -> GraphQLEngine | None:
        ...
