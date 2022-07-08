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

    _logger: logging.Logger

    _store: dict[str, aiohttp.ClientResponse | asyncio.Task]
    _queue: list[asyncio.Task]
    _session: aiohttp.ClientSession | None

    @staticmethod
    def hash(request: IRequest) -> str:
        key = hash(hash(request.url) + hash(request.method)) & 0xffffffff

        data = 0
        for k, v in request.kwargs.items():
            data += hash(f'{k},{str(v)}')

        return str((key + data) & 0xffffffff)

    @abstractmethod
    async def put(
        self,
        req: IRequest,
        key: str,
    ) -> None:
        ...

    def get(self, key: str) -> aiohttp.ClientResponse:
        return self._store[key]

    @abstractmethod
    async def send_request(
        self,
        request: IRequest,
        key: str,
    ) -> None:
        ...

    @abstractmethod
    async def consume_bucket(self) -> None:
        ...

    @abstractmethod
    async def open_session(self) -> None:
        ...

    @abstractmethod
    async def close_session(self) -> None:
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
