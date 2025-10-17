from typing import Any

import instructor
from anthropic import Anthropic
from openai import OpenAI
from pydantic import BaseModel

from python_llm_factory.config.base_settings import LLMProviderSettings
from python_llm_factory.consts.provider import LLMProvider


class LLMFactory:
    def __init__(self, settings: LLMProviderSettings) -> None:
        self.settings = settings
        self.client = self._initialize_client()

    def _initialize_client(self) -> Any:
        if self.settings.provider == LLMProvider.OPENAI:
            return instructor.from_openai(OpenAI(api_key=self.settings.api_key))
        if self.settings.provider == LLMProvider.ANTHROPIC:
            return instructor.from_anthropic(Anthropic(api_key=self.settings.api_key))
        if self.settings.provider == LLMProvider.GEMINI:
            return instructor.from_openai(
                OpenAI(base_url=self.settings.base_url, api_key=self.settings.api_key),
                mode=instructor.Mode.JSON,
            )
        if self.settings.provider == LLMProvider.LLAMA:
            return instructor.from_openai(
                OpenAI(base_url=self.settings.base_url, api_key=self.settings.api_key),
                mode=instructor.Mode.JSON,
            )
        raise ValueError(f"Unsupported LLM provider: {self.settings.provider}")

    def completions_create(
        self,
        response_model: type[BaseModel] | None,
        messages: list[dict[str, str]],
        model: str | None = None,
        temperature: float | None = None,
        max_retries: int | None = None,
        max_tokens: int | None = None,
        functions: list[dict[str, Any]] | None = None,
        function_call: str | None = None,
    ) -> Any:
        completion_params = {
            "model": model or self.settings.default_model,
            "temperature": temperature or self.settings.temperature,
            "max_retries": max_retries or self.settings.max_retries,
            "max_tokens": max_tokens or self.settings.max_tokens,
            "response_model": response_model,
            "messages": messages,
        }

        if self.settings.provider == LLMProvider.OPENAI:
            if functions:
                completion_params["functions"] = functions
            if function_call:
                completion_params["function_call"] = function_call

        return self.client.chat.completions.create(**completion_params)
