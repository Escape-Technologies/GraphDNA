# github_directory: strawberry-graphql/strawberry, stars: 2400, last_update: 2022-07-10
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Strawberry(IGQLQuery):

    score_factor = 0.54
    genetics = {
        'query @deprecated { __typename }': in_response_text('Directive \'@deprecated\' may not be used on query.'),
    }
