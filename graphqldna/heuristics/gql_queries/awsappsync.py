from graphqldna.detectors import is_present_in_textual_response
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Awsappsync(IGQLQuery):

    genetic_correlation = {
        'query @skip { __typename }': is_present_in_textual_response('MisplacedDirective'),
    }
