from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class DianaJl(IGQLQuery):

    genetic_correlation = {
        'query { __typename }': is_present_in_textual_response('Syntax Error GraphQL request (1:1) Unexpected Name \\"queryy\\"'),
    }
