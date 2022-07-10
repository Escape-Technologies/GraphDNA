from graphqldna.detectors import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Ariadne(IGQLQuery):

    genetics = {
        '': in_response_text('The query must be a string.'),
        'query { __typename @abc }': in_response_text('Unknown directive \'@abc\'.'),
    }
