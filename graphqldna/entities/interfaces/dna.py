# pylint: disable=missing-function-docstring,missing-class-docstring

"""Manage the dna interfaces."""

import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Any

import aiohttp

from graphqldna.entities.engines import GraphQLEngine


class IRequest:

    url: str
    method: str
    kwargs: dict[str, Any]

    def __init__(
        self,
        url: str,
        method: str,
        kwargs: dict[str, Any] = None,
    ) -> None:
        self.url = url
        self.method = method or 'GET'
        self.kwargs = kwargs or {}


class IHTTPBucket(ABC):

    _store: dict[str, aiohttp.ClientResponse | asyncio.Task]
    _queue: list[asyncio.Task]
    _session: aiohttp.ClientSession | None

    @staticmethod
    @abstractmethod
    def hash(request: IRequest) -> str:
        ...

    @abstractmethod
    async def put(self, requests: list[IRequest]) -> None:
        ...

    @abstractmethod
    async def send_request(self, request: IRequest) -> None:
        ...

    @abstractmethod
    async def consume_bucket(self) -> None:
        ...

    @abstractmethod
    async def _open_session(self) -> None:
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
