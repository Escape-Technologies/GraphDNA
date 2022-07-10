from graphqldna.detectors.checkers import in_section
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Directus(IGQLQuery):

    genetics = {
        '': in_section('INVALID_PAYLOAD', 'code'),
    }
