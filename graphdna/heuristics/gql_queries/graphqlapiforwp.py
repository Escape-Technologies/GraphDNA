# github_directory: GraphQLAPI/graphql-api-for-wp, stars: 150, last_update: 2022-07-10
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class GraphQLAPIForWP(IGQLQuery):

    score_factor = 0.5
    genetics = {
        '': in_response_text('The query in the body is empty'),
        'query @doesnotexist { __typename }': in_response_text('No DirectiveResolver resolves directive with name \'doesnotexist\''),
        'query @skip { __typename }': in_response_text('Argument \'if\' cannot be empty, so directive \'skip\' has been ignored'),
        'query aa#aa { __typename }': in_response_text('Unexpected token \\"END\\"'),
        'query {alias1$1:__typename}': in_response_text('QueryRoot'),
    }
