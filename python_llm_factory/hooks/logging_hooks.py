from typing import Callable

from custom_python_logger import get_logger, json_pretty_format
from instructor.core import HookName

from python_llm_factory import LLMFactory

logger = get_logger(__name__)

def log_kwargs(**kwargs) -> None:
    logger.debug(f"Function called with kwargs: {json_pretty_format(kwargs)}")


def log_completion_response(response) -> None:
    logger.debug(f"Completion response: {json_pretty_format(response)}")


def add_logging_hooks(client: LLMFactory, handler: Callable) -> None:
    client.client.on(HookName.COMPLETION_KWARGS, handler)
    logger.info(f"Completion logging hook registered for {client.client.name}")


def stop_logging_hooks(client, handler):
    client.client.off(HookName.COMPLETION_KWARGS, handler)
    logger.info(f"Completion logging hook stopped for {client.client.name}")
