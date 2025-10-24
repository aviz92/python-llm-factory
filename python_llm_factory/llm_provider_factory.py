from typing import Any

from anthropic import Anthropic
from custom_python_logger import get_logger, json_pretty_format
from openai import OpenAI

from python_llm_factory.config.base_settings import LlmProviderSettings
from python_llm_factory.config.settings_ins import get_settings
from python_llm_factory.consts.provider import LlmProvider


class LlmProviderFactory:
    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    @staticmethod
    def initialize_client(settings: LlmProviderSettings) -> Any:
        kwargs = {
            "api_key": settings.api_key,
            "base_url": settings.base_url
        }

        provider_func_mapping = {
            LlmProvider.OPENAI: OpenAI,
            LlmProvider.ANTHROPIC: Anthropic,
            LlmProvider.GEMINI: OpenAI,
            LlmProvider.LLAMA: OpenAI,
        }
        if settings.provider not in provider_func_mapping:
            raise ValueError(f"Unsupported LLM provider: {settings.provider}")
        return provider_func_mapping[settings.provider](**kwargs)
