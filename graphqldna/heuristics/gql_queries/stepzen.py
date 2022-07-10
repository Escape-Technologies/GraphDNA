from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Stepzen(IGQLQuery):

    score_factor = 1
    genetics = {
        '': in_response_text('Must provide an operation.'),
    }
