from graphqldna.detectors import is_present_in_section
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Agoo(IGQLQuery):

    genetic_correlation = {
        'query { zzz }': is_present_in_section('code', 'eval error'),
    }
