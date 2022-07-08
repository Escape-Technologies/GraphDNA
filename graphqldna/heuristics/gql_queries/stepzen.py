from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Stepzen(IGQLQuery):

    genetics = {
        '': is_present_in_textual_response('Must provide an operation.'),
    }
