"""Handle DNA flow for a given GraphQL endpoint."""

import asyncio
import logging

import aiohttp

from graphqldna.entities import GraphQLEngine
from graphqldna.entities.interfaces import IGraphQLDNA
from graphqldna.entities.interfaces.dna import IHTTPBucket, IRequest
from graphqldna.heuristics import HeuristicsManager
from graphqldna.logger import setup_logger


def detect_engine(
    url: str,
    headers: dict[str, str] | None = None,
) -> GraphQLEngine | None:
    """Manage the engine detection flow."""

    dna = GraphQLDNA(url, headers)
    return asyncio.run(dna.run())


async def detect_engine_async(
    url: str,
    headers: dict[str, str] | None = None,
) -> GraphQLEngine | None:
    """Manage the engine detection flow asyncronously."""

    dna = GraphQLDNA(url, headers)
    return await dna.run()


class HTTPBucket(IHTTPBucket):

    """Defines a HTTP Bucket, which store procedeed requests.

    The goal is to send requests once.
    """

    def __init__(
        self,
        logger: logging.Logger,
        headers: dict[str, str] | None,
    ) -> None:
        self._store = {}
        self._queue = []
        self._session = None

        self._headers = headers or {}
        self._logger = logger

    async def put(
        self,
        req: IRequest,
        key: str,
    ) -> None:
        if not self._session:
            await self.open_session()

        if key not in self._store:
            task = asyncio.create_task(self.send_request(req, key))
            self._store[key] = task
            self._queue.append(task)

    def get(
        self,
        key: str,
    ) -> aiohttp.ClientResponse:
        value = self._store.get(key)
        assert isinstance(value, aiohttp.ClientResponse)
        return value

    async def send_request(
        self,
        request: IRequest,
        key: str,
    ) -> None:
        if not self._session:
            self._session = await self.open_session()

        self._store[key] = await self._session.request(
            request.method,
            request.url,
            **request.kwargs,
        )

    async def consume_bucket(self) -> None:
        self._logger.info(f'Consuming bucket of {len(self._queue)} requests.')

        for task in self._queue:
            await task

    async def open_session(self) -> aiohttp.ClientSession:
        self._session = aiohttp.ClientSession(headers=self._headers, )
        return self._session

    async def close_session(self) -> None:
        if not self._session:
            return

        await self._session.close()
        self._session = None


class GraphQLDNA(IGraphQLDNA):

    """Manage the DNA of the GraphQL endpoint."""

    def __init__(
        self,
        url: str,
        headers: dict[str, str] | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        """Init class."""

        self._url = url
        self._logger = logger or setup_logger()
        self._http_bucket = HTTPBucket(self._logger, headers)

        self._logger.info(f'Initializing GraphQLDNA for {url}.')

    async def run(self) -> GraphQLEngine | None:
        """Run a DNA test."""

        heuristics = HeuristicsManager(self._logger)
        heuristics.load()

        await heuristics.enqueue_requests(self._url, self._http_bucket)
        await self._http_bucket.consume_bucket()
        await heuristics.parse_requests(self._http_bucket)
        heuristics.display_results()

        await self._http_bucket.close_session()

        return heuristics.best_candidate
