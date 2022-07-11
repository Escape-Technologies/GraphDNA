# GraphDNA ![PyPI](https://img.shields.io/pypi/v/GraphDNA)

[![CI](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/ci.yaml/badge.svg)](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/ci.yaml) [![CD](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/cd.yaml/badge.svg)](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/cd.yaml)

![PyPI - License](https://img.shields.io/pypi/l/GraphDNA) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/GraphDNA)
![PyPI - Downloads](https://img.shields.io/pypi/dm/GraphDNA)

[View on pypi!](https://pypi.org/project/GraphDNA/)

## Getting Started

I takes only two simple step to fingerprint an endpoint using GraphDNA.

```bash
pip install graphdna
graphdna -u https://example.com/graphql
```

The full list of supported engines is [here](https://github.com/Escape-Technologies/GraphDNA/blob/main/graphdna/entities/engines.py).

## Documentation

```python
from graphdna import detect_engine, detect_engine_async
from graphdna.entities import GraphQLEngine

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
