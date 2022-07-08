from graphqldna.detectors import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Ariadne(IGQLQuery):

    genetic_correlation = {
        '': is_present_in_textual_response('The query must be a string.'),
        'query { __typename @abc }': is_present_in_textual_response("Unknown directive '@abc'."),
    }
