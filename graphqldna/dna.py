"""Handle DNA flow for a given GraphQL endpoint."""

from graphqldna.entities.interfaces import IGraphQLDNA


class GraphQLDNA(IGraphQLDNA):

    """Manage the DNA of the GraphQL endpoint."""

    def __init__(self, url: str) -> None:
        """Init class."""

        self._url = url

    async def run(self) -> None:
        """Run a DNA test."""

        print(f'Running DNA test for {self._url}')
