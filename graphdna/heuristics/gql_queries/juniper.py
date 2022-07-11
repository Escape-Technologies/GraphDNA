# github_directory: graphql-rust/juniper, stars: 4595, last_update: 2022-07-10
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Juniper(IGQLQuery):

    score_factor = 0.58
    genetics = {
        '': in_response_text('Unexpected end of input'),
        'queryy { __typename }': in_response_text('Unexpected \\"queryy\\"'),
    }
