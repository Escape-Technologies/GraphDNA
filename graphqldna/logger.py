"""Manage logging flow."""

import os
import logging
import json_log_formatter  # type: ignore[import]


# pylint: disable=too-few-public-methods
class JSONFormat(json_log_formatter.JSONFormatter):

    """Overload the json formater."""

    def json_record(self, message, extra, record):  # type: ignore[no-untyped-def]
        """Add level and environment to the log record."""

        extra['level'] = (record.levelname or '').lower()
        extra['pathname'] = record.pathname or ''
        extra['lineno'] = record.lineno or ''

        return super().json_record(message, extra, record)


def install_logger() -> None:
    """Install logger."""

    handlers = {
        'console': logging.StreamHandler(),
        'json': logging.StreamHandler(),
    }
    handlers['json'].setFormatter(JSONFormat())
    handlers['console'].setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s'))

    log_format = os.getenv('LOG_FORMAT', 'console')

    logging.getLogger().addHandler(handlers[log_format])
    logging.getLogger().setLevel(logging.DEBUG)

    # Ignore asyncio debug logs
    logging.getLogger('asyncio').setLevel(logging.ERROR)


def setup_logger(name: str | None = None) -> logging.Logger:
    """Setup logger."""

    name = name or 'graphqldna'
    logger = logging.getLogger(name)

    if not logging.getLogger().hasHandlers():
        install_logger()

    return logger