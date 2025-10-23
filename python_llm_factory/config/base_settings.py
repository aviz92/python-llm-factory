from pydantic_settings import BaseSettings

from python_llm_factory.consts.provider import LlmProvider


class LlmProviderSettings(BaseSettings):
    provider: LlmProvider | None = None
    base_url: str | None = None
    api_key: str | None = None
    default_model: str | None = None

    temperature: float = 0
    max_tokens: int | None = None
    max_retries: int = 3
