from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Flutter(IGQLQuery):

    genetics = {
        'query { __typename @deprecated }': in_response_text('Directive \\"deprecated\\" may not be used on FIELD.'),
    }
