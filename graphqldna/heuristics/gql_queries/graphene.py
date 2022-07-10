from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Graphene(IGQLQuery):

    genetics = {
        'aaa': in_response_text('Syntax Error GraphQL (1:1)'),
    }
