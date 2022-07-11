# github_directory: webonyx/graphql-php, stars: 4339, last_update: 2022-07-10
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class GraphQLPHP(IGQLQuery):

    score_factor = 0.5700000000000001
    genetics = {
        'query ! {__typename}': in_response_text('Syntax Error: Cannot parse the unexpected character \\"?\\".'),
        'query @deprecated {__typename}': in_response_text('Directive \\"deprecated\\" may not be used on \\"QUERY\\".'),
    }
