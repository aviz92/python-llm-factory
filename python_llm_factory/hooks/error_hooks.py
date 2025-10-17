from typing import Callable

from instructor.core import HookName

from python_llm_factory import LLMFactory


def log_exception(exception: Exception):
    print(f"An exception occurred: {str(exception)}")


def add_error_hooks(client: LLMFactory, handler: Callable):
    client.client.on(HookName.COMPLETION_ERROR, handler)


def stop_error_hooks(client: LLMFactory, handler: Callable):
    client.client.off(HookName.COMPLETION_ERROR, handler)


def clear_error_hooks(client: LLMFactory):
    client.client.remove_all_listeners(HookName.COMPLETION_ERROR)
