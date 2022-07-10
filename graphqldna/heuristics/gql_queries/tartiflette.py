from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Tartiflette(IGQLQuery):

    genetics = {
        'query @a { __typename }': in_response_text('Unknow Directive < @a >.'),
        'query @skip { __typename }': in_response_text('Unknow Directive < @a >.'),
        'query { gqldna }': in_response_text('Field gqldna doesn\'t exist on Query'),
        'query { __typename @deprecated }': in_response_text('Directive < @deprecated > is not used in a valid location.'),
        'queryy { __typename }': in_response_text('syntax error, unexpected IDENTIFIER'),
    }
