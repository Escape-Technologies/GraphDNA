"""Manage logging flow."""

import logging
import os
from typing import Optional

import json_log_formatter  # type: ignore[import]


class JSONFormat(json_log_formatter.JSONFormatter):

    """Overload the json formater."""

    def json_record(self, message, extra, record):  # type: ignore[no-untyped-def]
        """Add level and environment to the log record."""

        extra['level'] = (record.levelname or '').lower()
        extra['pathname'] = record.pathname or ''
        extra['lineno'] = record.lineno or ''

        return super().json_record(message, extra, record)


def install_logger(logger: logging.Logger) -> None:
    """Install logger."""

    handlers = {
        'console': logging.StreamHandler(),
        'json': logging.StreamHandler(),
    }
    handlers['json'].setFormatter(JSONFormat())
    handlers['console'].setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s'))

    log_format = os.getenv('LOG_FORMAT', 'console')

    logger.addHandler(handlers[log_format])
    logger.setLevel(logging.DEBUG)

    # Ignore asyncio debug logs
    logging.getLogger('asyncio').setLevel(logging.ERROR)


def setup_logger(name: Optional[str] = None) -> logging.Logger:
    """Setup logger."""

    name = name or 'graphdna'
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        install_logger(logger)

    return logger
