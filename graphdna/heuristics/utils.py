from importlib import import_module
from pathlib import Path
from pkgutil import iter_modules
from types import ModuleType
from typing import List


def find_engine(
    engine: str,
    possibilities: List[str],
) -> str:
    for p in possibilities:
        if engine == p.lower():
            return p

    raise ValueError(f'Unknown engine `{engine}`, possibilities: {possibilities}')


def import_heuristics(
    pkg_file: str,
    pkg_name: str,
) -> List[ModuleType]:
    pkg_path = str(Path(pkg_file).parent.absolute())

    filenames = [filename for _, filename, _ in iter_modules([pkg_path])]

    return [import_module(f'{pkg_name}.{filename}') for filename in filenames]
