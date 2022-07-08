from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Sangria(IGQLQuery):

    genetic_correlation = {
        'queryy { __typename }':
            is_present_in_textual_response(
                'Syntax error while parsing GraphQL query. Invalid input \\"queryy\\", expected ExecutableDefinition or TypeSystemDefinition'
            ),
    }
