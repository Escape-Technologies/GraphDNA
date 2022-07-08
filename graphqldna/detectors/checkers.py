import functools
from typing import Awaitable

import aiohttp


def is_present_in_textual_response(data: str | list[str]) -> Awaitable:

    async def __internal(
        data: str | list[str],
        response: aiohttp.ClientResponse = None,
    ) -> bool:

        assert response, 'Response is required.'

        if isinstance(data, str):
            data = [data]

        response_text = await response.text()
        return any(text in response_text for text in data)

    return functools.partial(__internal, data)
