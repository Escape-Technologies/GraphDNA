from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class GraphQLGo(IGQLQuery):

    genetic_correlation = {
        '': is_present_in_textual_response('Must provide an operation.'),
        'query  { __typename {}': is_present_in_textual_response('Unexpected empty IN'),
        'query { __typename }': is_present_in_textual_response('RootQuery'),
    }
