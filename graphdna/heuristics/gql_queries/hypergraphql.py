# github_directory: hypergraphql/hypergraphql, stars: 146, last_update: 2022-07-10
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class HyperGraphQL(IGQLQuery):

    score_factor = 0.5
    genetics = {
        'query {alias1:__typename @deprecated}': in_response_text('Validation error of type UnknownDirective: Unknown directive deprecated @ \'__typename\''),
        'zzz { __typename }': in_response_text('Validation error of type InvalidSyntax: Invalid query syntax.'),
    }
