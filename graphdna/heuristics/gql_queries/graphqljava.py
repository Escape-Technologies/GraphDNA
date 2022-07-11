# github_directory: graphql-java/graphql-java, stars: 5539, last_update: 2022-07-10
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class GraphQLJava(IGQLQuery):

    score_factor = 0.59
    genetics = {
        '':
            in_response_text('Invalid Syntax : offending token \'<EOF>\''),
        'query @aaa@aaa { __typename }':
            in_response_text('Validation error of type DuplicateDirectiveName: Directives must be uniquely named within a location.'),
        'query { __typename }':
            in_response_text('Invalid Syntax : offending token \'queryy\''),
    }
