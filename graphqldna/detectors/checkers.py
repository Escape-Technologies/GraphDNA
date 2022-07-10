import functools
import json

import aiohttp


def in_response_text(data: str | list[str]) -> functools.partial:

    if isinstance(data, str):
        data = [data]

    async def __internal(
        data: list[str],
        response: aiohttp.ClientResponse = None,
    ) -> bool:

        assert response, 'Response is required.'

        response_text = await response.text()
        return any(text in response_text for text in data)

    return functools.partial(__internal, data)


def in_section(
    section: str,
    data: str | list[str],
) -> functools.partial:
    if isinstance(data, str):
        data = [data]

    async def __internal(
        section: str,
        data: list[str],
        response: aiohttp.ClientResponse = None,
    ) -> bool:

        assert response, 'Response is required.'

        response_json = await response.json()
        if section not in response_json:
            return False

        section_text = json.dumps(response_json[section])
        return any(text in section_text for text in data)

    return functools.partial(__internal, section, data)
