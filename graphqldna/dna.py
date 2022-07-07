"""Handle DNA flow for a given GraphQL endpoint."""

import asyncio
import logging

from graphqldna.entities import GraphQLEngine
from graphqldna.entities.interfaces import IGraphQLDNA
from graphqldna.logger import setup_logger


def detect_engine(url: str) -> GraphQLEngine:
    """Manage the engine detection flow."""

    dna = GraphQLDNA(url)
    return asyncio.run(dna.run())


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

        self._logger.info(f'Initializing GraphQLDNA for {url}.')

    async def run(self) -> GraphQLEngine:
        """Run a DNA test."""

        ...
