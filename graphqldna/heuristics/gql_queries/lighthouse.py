from graphqldna.detectors.checkers import in_response_text, in_section
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Lighthouse(IGQLQuery):

    genetics = {
        'query {__typename @include(if: falsee)}': [
            in_response_text('Internal server error'),
            in_section('category', 'internal'),
        ],
    }
