from pydantic_settings import BaseSettings


class LlmProviderSettings(BaseSettings):
    temperature: float = 0
    max_tokens: int | None = None
    max_retries: int = 3
