from functools import lru_cache

from pydantic_settings import BaseSettings

from python_llm_factory.config.anthropic_settings import AnthropicSettings
from python_llm_factory.config.gemini_settings import GeminiSettings
from python_llm_factory.config.llama_settings import LlamaSettings
from python_llm_factory.config.open_ai_settings import OpenAISettings


class Settings(BaseSettings):
    app_name: str = "GenAI Project Template"
    openai: OpenAISettings = OpenAISettings()
    anthropic: AnthropicSettings = AnthropicSettings()
    gemini: GeminiSettings = GeminiSettings()
    llama: LlamaSettings = LlamaSettings()


@lru_cache
def get_settings() -> Settings:
    return Settings()
