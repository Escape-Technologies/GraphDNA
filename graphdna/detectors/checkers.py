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
        if not response_text:
            return False
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
        if response_json or section not in response_json:
            return False

        section_text = json.dumps(response_json[section])
        return any(text in section_text for text in data)

    return functools.partial(__internal, section, data)


def has_json_key(sections: str | list[str]) -> functools.partial:

    if isinstance(sections, str):
        sections = [sections]

    async def __internal(
        sections: list[str],
        response: aiohttp.ClientResponse = None,
    ) -> bool:

        assert response, 'Response is required.'

        response_json = await response.json()
        if not response_json:
            return False
        return all(section in response_json for section in sections)

    return functools.partial(__internal, sections)
