from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class GQLGen(IGQLQuery):

    genetic_correlation = {
        'query { __typename {}': is_present_in_textual_response('Directive \\"deprecated\\" may not be used on FIELD.'),
        'query { alias^_:__typename {}': is_present_in_textual_response('Expected Name, found <Invalid>')
    }
