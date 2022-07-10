from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class HyperGraphQL(IGQLQuery):

    genetics = {
        'query {alias1:__typename @deprecated}': in_response_text('Validation error of type UnknownDirective: Unknown directive deprecated @ \'__typename\''),
        'zzz { __typename }': in_response_text('Validation error of type InvalidSyntax: Invalid query syntax.'),
    }
