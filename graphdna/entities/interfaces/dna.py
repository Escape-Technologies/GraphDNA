import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

import aiohttp

from graphdna.entities.engines import GraphQLEngine


class IRequest:

    url: str
    method: str
    kwargs: Dict[str, Any]

    def __init__(
        self,
        url: str,
        method: str,
        kwargs: Dict[str, Any] = None,
    ) -> None:
        self.url = url
        self.method = method or 'GET'
        self.kwargs = kwargs or {}

        self.kwargs['allow_redirects'] = False
        self.kwargs['timeout'] = 3


class IHTTPBucket(ABC):

    _headers: Dict[str, str]
    _store: Dict[str, Union[aiohttp.ClientResponse, asyncio.Task, None]]
    _queue: List[asyncio.Task]

    _url: str
    _base_url: str

    _session: Optional[aiohttp.ClientSession]
    _logger: logging.Logger

    @staticmethod
    def hash(request: IRequest) -> str:
        key = hash(hash(request.url) + hash(request.method))

        data = 0
        for k, v in request.kwargs.items():
            data += hash(f'{k},{str(v)}')

        return str((key + data) & 0xffffffff)

    @abstractmethod
    async def put(
        self,
        req: IRequest,
    ) -> str:
        ...

    @abstractmethod
    def get(
        self,
        key: str,
    ) -> Optional[aiohttp.ClientResponse]:
        ...

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
    async def open_session(self) -> aiohttp.ClientSession:
        ...

    @abstractmethod
    async def close_session(self) -> None:
        ...


class IGraphDNA(ABC):

    _url: str
    _logger: logging.Logger
    _http_bucket: IHTTPBucket

    @property
    def url(self) -> str:
        return self._url

    @abstractmethod
    async def run(self) -> Optional[GraphQLEngine]:
        ...
