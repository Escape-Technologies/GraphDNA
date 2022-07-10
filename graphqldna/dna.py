"""Handle DNA flow for a given GraphQL endpoint."""

import asyncio
import logging

from graphqldna.entities import GraphQLEngine
from graphqldna.entities.interfaces import IGraphQLDNA
from graphqldna.heuristics import HeuristicsManager
from graphqldna.http import HTTPBucket
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
        self._http_bucket = HTTPBucket(
            self._logger,
            self._url,
            headers,
        )

        self._logger.info(f'Initializing GraphQLDNA for {url}.')

    async def run(self) -> GraphQLEngine | None:
        """Manage DNA test flow."""

        heuristics = HeuristicsManager(self._logger)
        heuristics.load()

        await heuristics.enqueue_requests(self._url, self._http_bucket)
        await self._http_bucket.consume_bucket()
        await heuristics.parse_requests(self._http_bucket)
        heuristics.display_results()

        await self._http_bucket.close_session()

        return heuristics.best_candidate
