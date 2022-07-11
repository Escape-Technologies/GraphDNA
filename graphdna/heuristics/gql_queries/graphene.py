# github_directory: graphql-python/graphene, stars: 7291, last_update: 2022-07-10
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Graphene(IGQLQuery):

    score_factor = 0.62
    genetics = {
        'aaa': in_response_text('Syntax Error GraphQL (1:1)'),
    }
