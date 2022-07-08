from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class GraphQLJava(IGQLQuery):

    genetic_correlation = {
        '':
            is_present_in_textual_response("Invalid Syntax : offending token '<EOF>'"),
        'query @aaa@aaa { __typename }':
            is_present_in_textual_response('Validation error of type DuplicateDirectiveName: Directives must be uniquely named within a location.'),
        'query { __typename }':
            is_present_in_textual_response("Invalid Syntax : offending token 'queryy'"),
    }
