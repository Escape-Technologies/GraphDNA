from graphqldna.detectors import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Apollo(IGQLQuery):

    genetics = {
        'query @deprecated { __typename }':
            in_response_text([
                'Directive \\\"@deprecated\\\" may not be used on QUERY.',
                'Directive \\\"deprecated\\\" may not be used on QUERY.',
            ]),
        'query @skip { __typename }':
            in_response_text([
                'Directive \\\"@skip\\\" argument \\\"if\\\" of type \\\"Boolean!\\\" is required, but it was not provided',
                'Directive \\\"skip\\\" argument \\\"if\\\" of type \\\"Boolean!\\\" is required, but it was not provided'
            ])
    }
