"""Handle DNA flow for a given GraphQL endpoint."""

import asyncio
import logging
from typing import Dict, Optional

from graphdna.entities import GraphQLEngine
from graphdna.entities.interfaces import IGraphDNA
from graphdna.heuristics import HeuristicsManager
from graphdna.http import HTTPBucket
from graphdna.logger import setup_logger


def detect_engine(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    logger: Optional[logging.Logger] = None,
) -> Optional[GraphQLEngine]:
    """Manage the engine detection flow."""

    dna = GraphDNA(
        url,
        headers=headers,
        logger=logger,
    )
    return asyncio.run(dna.run())


async def detect_engine_async(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    logger: Optional[logging.Logger] = None,
) -> Optional[GraphQLEngine]:
    """Manage the engine detection flow asyncronously."""

    dna = GraphDNA(
        url,
        headers=headers,
        logger=logger,
    )
    return await dna.run()


class GraphDNA(IGraphDNA):

    """Manage the DNA of the GraphQL endpoint."""

    def __init__(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        """Init class."""

        self._url = url
        self._logger = logger or setup_logger()
        self._http_bucket = HTTPBucket(
            self._logger,
            self._url,
            headers,
        )
        self._logger.info(f'Initializing GraphDNA for {url}.')

    async def run(self) -> Optional[GraphQLEngine]:
        """Manage DNA test flow."""

        heuristics = HeuristicsManager(self._logger)
        heuristics.load()

        await heuristics.enqueue_requests(self._http_bucket)
        await self._http_bucket.consume_bucket()
        await heuristics.parse_requests(self._http_bucket)
        heuristics.display_results()

        await self._http_bucket.close_session()

        return heuristics.best_candidate
