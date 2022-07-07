"""Manage the dna interfaces."""

import logging

from graphqldna.entities.engines import GraphQLEngine


class IGraphQLDNA:

    """Provide the GraphQLDNA interface."""

    _url: str
    _logger: logging.Logger

    @property
    def url(self) -> str:
        """Get the URL."""

        return self._url

    async def run(self) -> GraphQLEngine:
        """Run the DNA."""

        raise NotImplementedError()
