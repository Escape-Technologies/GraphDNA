# pylint: disable=missing-function-docstring,missing-class-docstring

"""Manage the dna interfaces."""

import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Any

import aiohttp

from graphqldna.entities.engines import GraphQLEngine


class IHTTPBucket(ABC):

    _store: dict[str, aiohttp.ClientResponse]
    _queue: list[asyncio.Task]

    @staticmethod
    @abstractmethod
    def hash(url: str, method: str, *args: Any, **kwargs: dict[str, Any]) -> str:
        ...

    @abstractmethod
    def put(self) -> None:
        ...

    @abstractmethod
    async def consume_bucket(self) -> None:
        ...


class IGraphQLDNA(ABC):

    _url: str
    _logger: logging.Logger
    _http_bucket: IHTTPBucket

    @property
    def url(self) -> str:
        return self._url

    @abstractmethod
    async def run(self) -> GraphQLEngine:
        ...
