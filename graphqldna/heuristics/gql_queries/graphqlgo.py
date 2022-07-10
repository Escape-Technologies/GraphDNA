from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class GraphQLGo(IGQLQuery):

    genetics = {
        '': in_response_text('Must provide an operation.'),
        'query  { __typename {}': in_response_text('Unexpected empty IN'),
        'query { __typename }': in_response_text('RootQuery'),
    }
