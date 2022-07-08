from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class GraphQLAPIForWP(IGQLQuery):

    genetics = {
        '': is_present_in_textual_response('The query in the body is empty'),
        'query @doesnotexist { __typename }': is_present_in_textual_response('No DirectiveResolver resolves directive with name \'doesnotexist\''),
        'query @skip { __typename }': is_present_in_textual_response('Argument \'if\' cannot be empty, so directive \'skip\' has been ignored'),
        'query aa#aa { __typename }': is_present_in_textual_response('Unexpected token \\"END\\"'),
        'query {alias1$1:__typename}': is_present_in_textual_response('QueryRoot'),
    }
