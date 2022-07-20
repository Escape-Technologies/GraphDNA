# github_directory: 99designs/gqlgen, stars: 7741, last_update: 2022-07-10
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class GQLGen(IGQLQuery):

    score_factor = 0.63
    score = 200
    genetics = {
        'query  { __typename {}': in_response_text('GRAPHQL_PARSE_FAILED'),
        'query {enumInInput(input: {enum: INVALID})}': in_response_text('GRAPHQL_VALIDATION_FAILED'),
        'query { alias^_:__typename {}': in_response_text('Expected Name, found <Invalid>')
    }
