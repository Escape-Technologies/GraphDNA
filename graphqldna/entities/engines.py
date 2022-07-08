"""Manage engines entities."""

from enum import Enum, unique


@unique
class GraphQLEngine(Enum):

    """Represent GraphQL Engines."""

    ARIADNE = 'Ariadne'
    APOLLO = 'Apollo'
    AWSAPPSYNC = 'Awsappsync'
