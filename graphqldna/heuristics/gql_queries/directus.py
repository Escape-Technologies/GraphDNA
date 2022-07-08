from graphqldna.detectors.checkers import is_present_in_section
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Directus(IGQLQuery):

    genetics = {
        '': is_present_in_section('INVALID_PAYLOAD', 'code'),
    }
