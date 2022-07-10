from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class GraphQLJava(IGQLQuery):

    genetics = {
        '':
            in_response_text('Invalid Syntax : offending token \'<EOF>\''),
        'query @aaa@aaa { __typename }':
            in_response_text('Validation error of type DuplicateDirectiveName: Directives must be uniquely named within a location.'),
        'query { __typename }':
            in_response_text('Invalid Syntax : offending token \'queryy\''),
    }
