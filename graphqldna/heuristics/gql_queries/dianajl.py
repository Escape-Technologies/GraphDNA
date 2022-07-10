from graphqldna.detectors.checkers import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class DianaJl(IGQLQuery):

    genetics = {
        'query { __typename }': in_response_text('Syntax Error GraphQL request (1:1) Unexpected Name \\"queryy\\"'),
    }
