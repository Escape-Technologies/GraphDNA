from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Ruby(IGQLQuery):

    genetic_correlation = {
        'query @deprecated { __typename }':
            is_present_in_textual_response('\'@deprecated\' can\'t be applied to queries'),
        'query @skip { __typename }':
            is_present_in_textual_response('\'@skip\' can\'t be applied to queries (allowed: fields, fragment spreads, inline fragments)'),
        'query { __typename @skip }':
            is_present_in_textual_response('Directive \'skip\' is missing required arguments: if'),
        'query { __typename {}':
            is_present_in_textual_response('Parse error on \\"}\\" (RCURLY)')
    }
