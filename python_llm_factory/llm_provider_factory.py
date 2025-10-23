from typing import Any

from anthropic import Anthropic
from custom_python_logger import get_logger, json_pretty_format
from openai import OpenAI

from python_llm_factory.config.base_settings import LLMProviderSettings
from python_llm_factory.consts.provider import LLMProvider


class LLMProviderFactory:
    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    def initialize_client(self, settings: LLMProviderSettings) -> Any:
        self.logger.debug(f"Initializing client with settings: {json_pretty_format(settings.__dict__)}")

        kwargs = {
            "api_key": settings.api_key,
            "base_url": settings.base_url
        }

        provider_func_mapping = {
            LLMProvider.OPENAI: OpenAI,
            LLMProvider.ANTHROPIC: Anthropic,
            LLMProvider.GEMINI: OpenAI,
            LLMProvider.LLAMA: OpenAI,
        }
        if settings.provider not in provider_func_mapping:
            raise ValueError(f"Unsupported LLM provider: {settings.provider}")
        return provider_func_mapping[settings.provider](**kwargs)
