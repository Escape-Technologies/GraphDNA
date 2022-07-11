# GraphQL DNA ![PyPI](https://img.shields.io/pypi/v/GraphQLDNA)

[![CI](https://github.com/Escape-Technologies/GraphQLDNA/actions/workflows/ci.yaml/badge.svg)](https://github.com/Escape-Technologies/GraphQLDNA/actions/workflows/ci.yaml) [![CD](https://github.com/Escape-Technologies/GraphQLDNA/actions/workflows/cd.yaml/badge.svg)](https://github.com/Escape-Technologies/GraphQLDNA/actions/workflows/cd.yaml)

![PyPI - License](https://img.shields.io/pypi/l/GraphQLDNA) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/GraphQLDNA)
![PyPI - Downloads](https://img.shields.io/pypi/dm/GraphQLDNA)

[View on pypi!](https://pypi.org/project/GraphQLDNA/)

## Getting Started

I takes only two simple step to fingerprint an endpoint using GraphQL DNA.

```bash
pip install graphqldna
graphqldna -u https://example.com/graphql
```

The full list of supported engines is [here](https://github.com/Escape-Technologies/GraphQLDNA/blob/main/graphqldna/entities/engines.py).

## Documentation

```python
from graphqldna import detect_engine, detect_engine_async
from graphqldna.entities import GraphQLEngine

def detect_engine(
    url: str,
    headers: dict[str, str] | None = None,
    logger: logging.Logger | None = None,
) -> GraphQLEngine | None:
    ...


async def detect_engine_async(
    url: str,
    headers: dict[str, str] | None = None,
    logger: logging.Logger | None = None,
) -> GraphQLEngine | None:
    ...
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
