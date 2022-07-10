from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Juniper(IGQLQuery):

    genetics = {
        '': in_response_text('Unexpected end of input'),
        'queryy  {__typename}': in_response_text('Unexpected \\"queryy\\"'),
    }
