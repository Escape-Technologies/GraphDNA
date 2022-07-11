# github_directory: apollographql/apollo-server, stars: 12730, last_update: 2022-07-10
from graphdna.detectors import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Apollo(IGQLQuery):

    score_factor = 0.71
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
