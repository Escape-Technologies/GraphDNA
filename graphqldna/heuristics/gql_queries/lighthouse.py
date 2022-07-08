from graphqldna.detectors.checkers import is_present_in_section, is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Lighthouse(IGQLQuery):

    genetics = {
        'query {__typename @include(if: falsee)}': [
            is_present_in_textual_response('Internal server error'),
            is_present_in_section('category', 'internal'),
        ],
    }
