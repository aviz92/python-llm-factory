from typing import Any


from python_llm_factory.config.base_settings import LlmProviderSettings
from python_llm_factory.consts.provider import LlmProvider
from python_llm_factory.llm_provider_factory import LlmProviderFactory

from agno.models.google.gemini import Gemini
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat


class LlmAgnoFactory:
    def __init__(self, settings: LlmProviderSettings) -> None:
        self.settings = settings
        self.llm_provider_factory = LlmProviderFactory()
        self.client = self._initialize_model()

    def _initialize_model(self) -> Any:
        if self.settings.provider == LlmProvider.OPENAI:
            return OpenAIChat(id=self.settings.default_model, api_key=self.settings.api_key)
        if self.settings.provider == LlmProvider.ANTHROPIC:
            return Claude(id=self.settings.default_model, api_key=self.settings.api_key)
        if self.settings.provider == LlmProvider.GEMINI:
            return Gemini(id=self.settings.default_model, api_key=self.settings.api_key)
        raise ValueError(f"Unsupported LLM provider: {self.settings.provider}")
