from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class HyperGraphQL(IGQLQuery):

    genetic_correlation = {
        'query {alias1:__typename @deprecated}':
            is_present_in_textual_response('Validation error of type UnknownDirective: Unknown directive deprecated @ \'__typename\''),
        'zzz { __typename }':
            is_present_in_textual_response('Validation error of type InvalidSyntax: Invalid query syntax.'),
    }
