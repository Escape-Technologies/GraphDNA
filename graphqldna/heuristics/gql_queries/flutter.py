from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Flutter(IGQLQuery):

    genetics = {
        'query { __typename @deprecated }': is_present_in_textual_response('Directive \\"deprecated\\" may not be used on FIELD.'),
    }
