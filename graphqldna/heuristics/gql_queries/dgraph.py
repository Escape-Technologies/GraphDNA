from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class DGraph(IGQLQuery):

    genetics = {
        'query { __typename }': in_response_text('Not resolving __typename. There\'s no GraphQL schema in Dgraph. Use the /admin API to add a GraphQL schema'),
    }
