"""Manage engines entities."""

from enum import Enum, unique


@unique
class GraphQLEngine(Enum):

    """Represent GraphQL Engines"""

    ARIADNE = 'ariadne'
    APOLLO = 'apollo'
