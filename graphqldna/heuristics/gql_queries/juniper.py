from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Juniper(IGQLQuery):

    genetics = {
        '': is_present_in_textual_response('Unexpected end of input'),
        'queryy  {__typename}': is_present_in_textual_response('Unexpected \\"queryy\\"'),
    }
