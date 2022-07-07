"""Manage the dna interfaces."""


class IGraphQLDNA:

    """Provide the GraphQLDNA interface."""

    _url: str

    @property
    def url(self) -> str:
        """Get the URL."""

        return self._url

    async def run(self) -> None:
        """Run the DNA."""

        raise NotImplementedError()
