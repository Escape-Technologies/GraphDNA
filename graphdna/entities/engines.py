"""Manage engines entities."""

from enum import Enum, unique


@unique
class GraphQLEngine(Enum):

    """Represent GraphQL Engines."""

    AGOO = 'Agoo'
    APOLLO = 'Apollo'
    ARIADNE = 'Ariadne'
    AWSAPPSYNC = 'AWSAppSync'
    DGRAPH = 'DGraph'
    DIANAJL = 'DianaJl'
    DIRECTUS = 'Directus'
    FLUTTER = 'Flutter'
    GRAPHENE = 'Graphene'
    GRAPHQLAPIFORWP = 'GraphQLAPIForWP'
    GRAPHQLGO = 'GraphQLGo'
    GRAPHQLJAVA = 'GraphQLJava'
    GRAPHQLPHP = 'GraphQLPHP'
    GRAPHQLYOGA = 'GraphQLYoga'
    HASURA = 'Hasura'
    HYPERGRAPHQL = 'HyperGraphQL'
    JUNIPER = 'Juniper'
    LIGHTHOUSE = 'Lighthouse'
    QGLGEN = 'GQLGen'
    RUBY = 'Ruby'
    SANGRIA = 'Sangria'
    SHOPIFY = 'Shopify'
    STEPZEN = 'Stepzen'
    STRAWBERRY = 'Strawberry'
    TARTIFLETTE = 'Tartiflette'
    WPGRAPHQL = 'WPGraphQL'
