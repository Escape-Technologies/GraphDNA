from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class WPGraphQL(IGQLQuery):

    genetics = {
        '': in_response_text('GraphQL Request must include at least one of those two parameters: \\"query\\" or \\"queryId\\"'),
        'query {alias1$1:__typename}': in_response_text('GraphQL Debug logging is not active. To see debug logs, GRAPHQL_DEBUG must be enabled.'),
    }
