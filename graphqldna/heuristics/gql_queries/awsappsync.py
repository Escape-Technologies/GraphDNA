from graphqldna.detectors import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class AWSAppSync(IGQLQuery):

    genetics = {
        'query @skip { __typename }': is_present_in_textual_response('MisplacedDirective'),
    }
