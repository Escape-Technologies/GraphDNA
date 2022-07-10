# github_directory: nuwave/lighthouse, stars: 2920, last_update: 2022-07-10
from graphqldna.detectors.checkers import in_response_text, in_section
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Lighthouse(IGQLQuery):

    score_factor = 0.55
    genetics = {
        'query {__typename @include(if: falsee)}': [
            in_response_text('Internal server error'),
            in_section('category', 'internal'),
        ],
    }
