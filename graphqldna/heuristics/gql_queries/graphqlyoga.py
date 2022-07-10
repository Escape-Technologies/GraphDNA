from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class GraphQLYoga(IGQLQuery):

    genetics = {
        'subscription {__typename }': in_response_text([
            'asyncExecutionResult[Symbol.asyncIterator] is not a function',
            'Unexpected error.',
        ])
    }
