from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Sangria(IGQLQuery):

    genetics = {
        'queryy { __typename }':
            in_response_text('Syntax error while parsing GraphQL query. Invalid input \\"queryy\\", expected ExecutableDefinition or TypeSystemDefinition'),
    }
