from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class GraphQLPHP(IGQLQuery):

    genetic_correlation = {
        'query ! {__typename}': is_present_in_textual_response('Syntax Error: Cannot parse the unexpected character \\"?\\".'),
        'query @deprecated {__typename}': is_present_in_textual_response('Directive \\"deprecated\\" may not be used on \\"QUERY\\".'),
    }
