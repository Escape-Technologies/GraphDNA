from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Graphene(IGQLQuery):

    genetics = {
        'aaa': is_present_in_textual_response('Syntax Error GraphQL (1:1)'),
    }
