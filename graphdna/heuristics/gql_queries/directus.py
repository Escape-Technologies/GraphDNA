# github_directory: directus/directus, stars: 16802, last_update: 2022-07-10
from graphdna.detectors.checkers import in_section
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Directus(IGQLQuery):

    score_factor = 0.78
    genetics = {
        '': in_section('INVALID_PAYLOAD', 'code'),
    }
