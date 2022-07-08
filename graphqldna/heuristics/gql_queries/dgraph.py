from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class DGraph(IGQLQuery):

    genetic_correlation = {
        'query { __typename }':
            is_present_in_textual_response('Not resolving __typename. There\'s no GraphQL schema in Dgraph. Use the /admin API to add a GraphQL schema'),
    }
