# github_directory: neomatrixcode/Diana.jl, stars: 104, last_update: 2022-07-10
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class DianaJl(IGQLQuery):

    score_factor = 0.5
    genetics = {
        'query { __typename }': in_response_text('Syntax Error GraphQL request (1:1) Unexpected Name \\"queryy\\"'),
    }
