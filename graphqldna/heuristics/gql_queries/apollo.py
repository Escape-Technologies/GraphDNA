from graphqldna.detectors import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Apollo(IGQLQuery):

    genetics = {
        'query @deprecated { __typename }':
            is_present_in_textual_response([
                'Directive \\\"@deprecated\\\" may not be used on QUERY.',
                'Directive \\\"deprecated\\\" may not be used on QUERY.',
            ]),
        'query @skip { __typename }':
            is_present_in_textual_response([
                'Directive \\\"@skip\\\" argument \\\"if\\\" of type \\\"Boolean!\\\" is required, but it was not provided',
                'Directive \\\"skip\\\" argument \\\"if\\\" of type \\\"Boolean!\\\" is required, but it was not provided'
            ])
    }
