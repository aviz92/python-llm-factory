from functools import lru_cache

from pydantic_settings import BaseSettings

from python_llm_factory.config.anthropic_settings import AnthropicSettings
from python_llm_factory.config.gemini_settings import GeminiSettings
from python_llm_factory.config.llama_settings import LlamaSettings
from python_llm_factory.config.open_ai_settings import OpenAISettings


DEFAULT_APP_NAME = "GenAI Project Template"

class Settings(BaseSettings):
    app_name: str = DEFAULT_APP_NAME
    openai: OpenAISettings = OpenAISettings()
    anthropic: AnthropicSettings = AnthropicSettings()
    gemini: GeminiSettings = GeminiSettings()
    llama: LlamaSettings = LlamaSettings()


@lru_cache
def get_settings(name: str = DEFAULT_APP_NAME) -> Settings:
    return Settings(app_name=name)
