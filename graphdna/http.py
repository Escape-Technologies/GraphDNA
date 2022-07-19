import asyncio
import logging
from typing import Dict, Optional

import aiohttp

from graphdna.entities.interfaces.dna import IHTTPBucket, IRequest


class HTTPBucket(IHTTPBucket):

    """Defines a HTTP Bucket, which store procedeed requests.

    The goal is to send requests once.
    """

    def __init__(
        self,
        logger: logging.Logger,
        url: str,
        headers: Optional[Dict[str, str]],
    ) -> None:
        self._store = {}
        self._queue = []
        self._session = None

        self._url = url
        self._base_url = '/'.join(url.split('/')[0:3])
        self._headers = headers or {}
        self._logger = logger

    async def put(
        self,
        req: IRequest,
    ) -> str:
        if not self._session:
            await self.open_session()

        key = self.hash(req)
        if key not in self._store:
            task = asyncio.create_task(self.send_request(req, key))
            self._store[key] = task
            self._queue.append(task)

        return key

    def get(
        self,
        key: str,
    ) -> Optional[aiohttp.ClientResponse]:
        value = self._store.get(key)
        assert isinstance(value, aiohttp.ClientResponse) or value is None
        return value

    async def send_request(
        self,
        request: IRequest,
        key: str,
    ) -> None:
        if not self._session:
            self._session = await self.open_session()

        if '%%base_url%%' in request.url:
            request.url = request.url.replace(
                '%%base_url%%',
                self._base_url,
            )

        if '%%url%%' in request.url:
            request.url = request.url.replace(
                '%%url%%',
                self._url,
            )

        if self._logger.level < logging.DEBUG:
            self._logger.debug(f'[{request.method}] {request.url} {request.kwargs}')

        try:
            self._store[key] = await self._session.request(
                request.method,
                request.url,
                **request.kwargs,
            )
        except asyncio.exceptions.TimeoutError:
            self._logger.debug(f'[{request.method}] {request.url} timed out.')
            self._store[key] = None

    async def consume_bucket(self) -> None:
        self._logger.info(f'Consuming bucket of {len(self._queue)} requests.')

        for task in self._queue:
            await task

    async def open_session(self) -> aiohttp.ClientSession:
        self._session = aiohttp.ClientSession(headers=self._headers)
        return self._session

    async def close_session(self) -> None:
        if not self._session:
            return

        await self._session.close()
        self._session = None
