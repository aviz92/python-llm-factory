import os

from pydantic_settings import BaseSettings

from python_llm_factory.config.base_settings import LlmProviderSettings
from python_llm_factory.consts.provider import LlmProvider


class OpenAIBaseSettings(LlmProviderSettings):
    provider: str = LlmProvider.OPENAI.value
    # base_url: str | None = None
    api_key: str = os.getenv("OPENAI_API_KEY", "")


class Gpt4oSettings(OpenAIBaseSettings):
    default_model: str = "gpt-4o"
    temperature: float = 0.7


class OpenAISettings(BaseSettings):
    gpt_4o: LlmProviderSettings = Gpt4oSettings()
