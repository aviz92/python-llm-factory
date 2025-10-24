from pydantic_settings import BaseSettings

from python_llm_factory.config.base_settings import LlmProviderSettings
from python_llm_factory.consts.provider import LlmProvider


class LlamaBaseSettings(LlmProviderSettings):
    provider: str = LlmProvider.LLAMA.value
    base_url: str = "http://localhost:11434/v1"
    api_key: str = "key"  # required, but not used


class Llama3Settings(LlamaBaseSettings):
    default_model: str = "llama3"


class LlamaSettings(BaseSettings):
    llama3: LlmProviderSettings = Llama3Settings()
