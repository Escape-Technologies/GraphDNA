from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Hasura(IGQLQuery):

    genetics = {
        'query @cached {__typename}': in_response_text('query_root'),
        'query @skip {__typename}': in_response_text('directive \\"skip\\" is not allowed on a query'),
        'query { __schema }': in_response_text('missing selection set for \\"__Schema\\"'),
        'query { aa }': in_response_text('field \\"aaa\\" not found in type: \'query_root\''),
    }
