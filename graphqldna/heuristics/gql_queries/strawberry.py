from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Strawberry(IGQLQuery):

    genetics = {
        'query @deprecated { __typename }': in_response_text('Directive \'@deprecated\' may not be used on query.'),
    }
