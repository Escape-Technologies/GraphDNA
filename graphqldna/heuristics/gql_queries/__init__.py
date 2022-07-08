from graphqldna.entities.engines import GraphQLEngine
from graphqldna.entities.interfaces.heuristics import IGQLQuery
from graphqldna.heuristics.utils import import_heuristics


def find_engine(
    engine: str,
    possibilities: list[str],
) -> str:
    for p in possibilities:
        if engine == p.lower():
            return p
    raise ValueError(f'Unknown engine `{engine}`, possibilities: {possibilities}')


def import_gql_queries() -> list[IGQLQuery]:
    raw_heuritics = import_heuristics(
        __file__,
        __name__,
    )

    heuristics: list[IGQLQuery] = []
    for raw in raw_heuritics:
        engine = raw.__name__.split('.')[-1]
        engine = find_engine(engine, dir(raw))

        cls = eval(f'raw.{engine}')  # pylint: disable=eval-used
        cls.__engine__ = GraphQLEngine(engine)
        heuristics.append(cls)

    return heuristics
