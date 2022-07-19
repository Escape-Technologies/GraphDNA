"""Manage the heuristics interfaces."""

import functools
import logging
from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Dict, List, Optional, Tuple, Union

from graphdna.entities.engines import GraphQLEngine
from graphdna.entities.interfaces import IHTTPBucket
from graphdna.entities.interfaces.dna import IRequest

EvalMethods = Union[functools.partial, List[functools.partial]]


class IHeuristic(ABC):

    score: int = 100
    score_factor: float = 1.0

    def verify(self) -> bool:
        raise NotImplementedError


class IGQLQuery(IHeuristic):

    genetics: Dict[str, EvalMethods]


class IWebProperty(IHeuristic):

    requests: List[Tuple[IRequest, EvalMethods]]


class IHeuristicManager(ABC):

    _logger: logging.Logger

    @abstractmethod
    async def enqueue_requests(
        self,
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
    ) -> AsyncGenerator[Tuple[Any, GraphQLEngine], None]:
        ...


class IGQLQueriesManager(IHeuristicManager):

    _heuristics: List[IGQLQuery]


class IWebPropertiesManager(IHeuristicManager):

    _heuristics: List[IWebProperty]


class IHeuristicsManager(ABC):

    _logger: logging.Logger
    _candidates: Dict[GraphQLEngine, int]

    _gql_queries_manager: IHeuristicManager

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    async def enqueue_requests(
        self,
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
    def best_candidate(self) -> Optional[GraphQLEngine]:
        ...
