# github_directory: ohler55/agoo, stars: 790, last_update: 2022-07-10
from graphdna.detectors import in_section
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Agoo(IGQLQuery):

    score_factor = 0.51
    genetics = {
        'query { zzz }': in_section('code', 'eval error'),
    }
