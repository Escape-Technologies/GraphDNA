from graphqldna.detectors.checkers import is_present_in_section
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Directus(IGQLQuery):

    genetic_correlation = {
        '': is_present_in_section('INVALID_PAYLOAD', 'code'),
    }
