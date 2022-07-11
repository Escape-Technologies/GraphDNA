# github_directory: wp-graphql/wp-graphql, stars: 3261, last_update: 2022-07-10
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class WPGraphQL(IGQLQuery):

    score_factor = 0.55
    genetics = {
        '': in_response_text('GraphQL Request must include at least one of those two parameters: \\"query\\" or \\"queryId\\"'),
        'query {alias1$1:__typename}': in_response_text('GraphQL Debug logging is not active. To see debug logs, GRAPHQL_DEBUG must be enabled.'),
    }
