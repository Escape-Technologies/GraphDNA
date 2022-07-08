from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Hasura(IGQLQuery):

    genetic_correlation = {
        'query @cached {__typename}': is_present_in_textual_response('query_root'),
        'query @skip {__typename}': is_present_in_textual_response('directive \\"skip\\" is not allowed on a query'),
        'query { __schema }': is_present_in_textual_response('missing selection set for \\"__Schema\\"'),
        'query { aa }': is_present_in_textual_response('field \\"aaa\\" not found in type: \'query_root\''),
    }
