import os

from pydantic_settings import BaseSettings

from python_llm_factory.config.base_settings import LlmProviderSettings
from python_llm_factory.consts.provider import LlmProvider


class GeminiBaseSettings(LlmProviderSettings):
    provider: str = LlmProvider.GEMINI.value
    base_url: str = "https://generativelanguage.googleapis.com/v1beta/openai"
    api_key: str = os.getenv("GEMINI_API_KEY", "")
    max_tokens: int = 4096


class Gemini15FlashSettings(GeminiBaseSettings):
    default_model: str = "gemini-1.5-flash"


class Gemini25FlashSettings(GeminiBaseSettings):
    default_model: str = "gemini-2.5-flash"


class GeminiSettings(BaseSettings):
    gemini_1_5_flash: LlmProviderSettings = Gemini15FlashSettings()
    gemini_2_5_flash: LlmProviderSettings = Gemini25FlashSettings()
