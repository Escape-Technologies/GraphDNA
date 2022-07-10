from graphqldna.detectors import in_response_text
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class AWSAppSync(IGQLQuery):

    genetics = {
        'query @skip { __typename }': in_response_text('MisplacedDirective'),
    }
