from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class GQLGen(IGQLQuery):

    genetics = {
        'query { __typename {}': in_response_text('Directive \\"deprecated\\" may not be used on FIELD.'),
        'query { alias^_:__typename {}': in_response_text('Expected Name, found <Invalid>')
    }
