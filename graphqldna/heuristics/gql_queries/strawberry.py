from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Strawberry(IGQLQuery):

    genetics = {
        'query @deprecated { __typename }': is_present_in_textual_response('Directive \'@deprecated\' may not be used on query.'),
    }
