from graphqldna.detectors.checkers import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Tartiflette(IGQLQuery):

    genetics = {
        'query @a { __typename }': is_present_in_textual_response('Unknow Directive < @a >.'),
        'query @skip { __typename }': is_present_in_textual_response('Unknow Directive < @a >.'),
        'query { gqldna }': is_present_in_textual_response('Field gqldna doesn\'t exist on Query'),
        'query { __typename @deprecated }': is_present_in_textual_response('Directive < @deprecated > is not used in a valid location.'),
        'queryy { __typename }': is_present_in_textual_response('syntax error, unexpected IDENTIFIER'),
    }
