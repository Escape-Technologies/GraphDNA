import functools
import json
from typing import Awaitable

import aiohttp


def is_present_in_textual_response(data: str | list[str]) -> Awaitable:

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


def is_present_in_section(section: str, data: str | list[str]) -> Awaitable:
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
        return data in json.dumps(response_json[section])

    return functools.partial(__internal, section, data)
