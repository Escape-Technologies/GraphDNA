from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class WPGraphQL(IGQLQuery):

    genetics = {
        '': is_present_in_textual_response('GraphQL Request must include at least one of those two parameters: \\"query\\" or \\"queryId\\"'),
        'query {alias1$1:__typename}': is_present_in_textual_response('GraphQL Debug logging is not active. To see debug logs, GRAPHQL_DEBUG must be enabled.'),
    }
