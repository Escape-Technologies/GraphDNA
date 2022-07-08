"""Handle DNA flow for a given GraphQL endpoint."""

import asyncio
import logging

import aiohttp

from graphqldna.entities import GraphQLEngine
from graphqldna.entities.interfaces import IGraphQLDNA
from graphqldna.entities.interfaces.dna import IHTTPBucket, IRequest
from graphqldna.heuristics import HeuristicsManager
from graphqldna.logger import setup_logger


def detect_engine(url: str) -> GraphQLEngine:
    """Manage the engine detection flow."""

    dna = GraphQLDNA(url)
    return asyncio.run(dna.run())


async def detect_engine_async(url: str) -> GraphQLEngine:
    """Manage the engine detection flow asyncronously."""

    dna = GraphQLDNA(url)
    return await dna.run()


class HTTPBucket(IHTTPBucket):

    """Defines a HTTP Bucket, which store procedeed requests.

    The goal is to send requests once.
    """

    def __init__(
        self,
        logger: logging.Logger,
    ) -> None:
        self._logger = logger

        self._store = {}
        self._queue = []
        self._session = None

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

    async def send_request(
        self,
        request: IRequest,
        key: str,
    ) -> aiohttp.ClientResponse:

        self._store[key] = await self._session.request(
            request.method,
            request.url,
            **request.kwargs,
        )

    async def consume_bucket(self) -> None:
        self._logger.info(f'Consuming bucket of {len(self._queue)} requests.')

        for task in self._queue:
            await task

    async def open_session(self) -> None:
        self._session = aiohttp.ClientSession()

    async def close_session(self) -> None:
        await self._session.close()
        self._session = None


class GraphQLDNA(IGraphQLDNA):

    """Manage the DNA of the GraphQL endpoint."""

    def __init__(
        self,
        url: str,
        logger: logging.Logger | None = None,
    ) -> None:
        """Init class."""

        self._url = url
        self._logger = logger or setup_logger()
        self._http_bucket = HTTPBucket(self._logger)

        self._logger.info(f'Initializing GraphQLDNA for {url}.')

    async def run(self) -> GraphQLEngine:
        """Run a DNA test."""

        heuristics = HeuristicsManager(self._logger)
        heuristics.load()

        await heuristics.enqueue_requests(self._url, self._http_bucket)
        await self._http_bucket.consume_bucket()
        await heuristics.parse_requests(self._http_bucket)
        heuristics.display_results()

        await self._http_bucket.close_session()

        return heuristics.best_candidate
