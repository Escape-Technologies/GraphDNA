"""Handle DNA flow for a given GraphQL endpoint."""

import asyncio
import logging
from typing import Any

from graphqldna.entities import GraphQLEngine
from graphqldna.entities.interfaces import IGraphQLDNA
from graphqldna.entities.interfaces.dna import IHTTPBucket
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
class GraphQLDNA(IGraphQLDNA):

    """Manage the DNA of the GraphQL endpoint."""

    def __init__(
        self,
        url: str,
        logger: logging.Logger | None = None,
    ) -> None:
        """Init class."""

        self._logger.info(f'Initializing GraphQLDNA for {url}.')

        self._url = url
        self._logger = logger or setup_logger()

        self._http_bucket = HTTPBucket()

    async def run(self) -> GraphQLEngine:
        """Run a DNA test."""

        ...
