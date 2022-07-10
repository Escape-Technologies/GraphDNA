from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Ruby(IGQLQuery):

    genetics = {
        'query @deprecated { __typename }': in_response_text('\'@deprecated\' can\'t be applied to queries'),
        'query @skip { __typename }': in_response_text('\'@skip\' can\'t be applied to queries (allowed: fields, fragment spreads, inline fragments)'),
        'query { __typename @skip }': in_response_text('Directive \'skip\' is missing required arguments: if'),
        'query { __typename {}': in_response_text('Parse error on \\"}\\" (RCURLY)')
    }
