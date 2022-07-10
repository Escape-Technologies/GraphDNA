from graphqldna.detectors import in_section
from graphqldna.entities.interfaces.heuristics import IGQLQuery


class Agoo(IGQLQuery):

    genetics = {
        'query { zzz }': in_section('code', 'eval error'),
    }
