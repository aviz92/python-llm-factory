from typing import Callable

from custom_python_logger import json_pretty_format
from instructor.core import HookName

from python_llm_factory import LLMFactory


def log_kwargs(**kwargs) -> None:
    print(f"Function called with kwargs: {json_pretty_format(kwargs)}")


def log_completion_response(response) -> None:
    print(f"Completion response: {json_pretty_format(response)}")


def add_logging_hooks(client: LLMFactory, handler: Callable) -> None:
    client.client.on(HookName.COMPLETION_KWARGS, handler)


def stop_logging_hooks(client, handler):
    client.client.off(HookName.COMPLETION_KWARGS, handler)
