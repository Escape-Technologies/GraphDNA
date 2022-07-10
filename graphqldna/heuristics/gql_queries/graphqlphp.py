from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class GraphQLPHP(IGQLQuery):

    genetics = {
        'query ! {__typename}': in_response_text('Syntax Error: Cannot parse the unexpected character \\"?\\".'),
        'query @deprecated {__typename}': in_response_text('Directive \\"deprecated\\" may not be used on \\"QUERY\\".'),
    }
