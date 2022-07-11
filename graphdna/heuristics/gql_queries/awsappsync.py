from graphdna.detectors import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class AWSAppSync(IGQLQuery):

    score_factor = 1
    genetics = {
        'query @skip { __typename }': in_response_text('MisplacedDirective'),
    }
