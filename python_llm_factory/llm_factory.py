from enum import StrEnum
from typing import Any, Dict, List, Type, Optional

import instructor
from anthropic import Anthropic
from python_llm_factory.config.settings import get_settings
from openai import OpenAI
from pydantic import BaseModel


class LLMProvider(StrEnum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"
    LLAMA = "llama"


class LLMFactory:
    def __init__(self, provider: LLMProvider):
        self.provider = provider
        self.settings = getattr(get_settings(), provider)
        self.client = self._initialize_client()

    def _initialize_client(self) -> Any:
        if self.provider == LLMProvider.OPENAI:
            return instructor.from_openai(OpenAI(api_key=self.settings.api_key))
        if self.provider == LLMProvider.ANTHROPIC:
            return instructor.from_anthropic(Anthropic(api_key=self.settings.api_key))
        if self.provider == LLMProvider.GEMINI:
            return instructor.from_openai(
                OpenAI(base_url=self.settings.base_url, api_key=self.settings.api_key),
                mode=instructor.Mode.JSON,
            )
        if self.provider == LLMProvider.LLAMA:
            return instructor.from_openai(
                OpenAI(base_url=self.settings.base_url, api_key=self.settings.api_key),
                mode=instructor.Mode.JSON,
            )
        raise ValueError(f"Unsupported LLM provider: {self.provider}")

    def create_completion(
        self,
        response_model: Optional[Type[BaseModel]],
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_retries: Optional[int] = None,
        max_tokens: Optional[int] = None,
        functions: Optional[List[Dict[str, Any]]] = None,
        function_call: Optional[str] = None,
    ) -> Any:
        completion_params = {
            "model": model or self.settings.default_model,
            "temperature": temperature or self.settings.temperature,
            "max_retries": max_retries or self.settings.max_retries,
            "max_tokens": max_tokens or self.settings.max_tokens,
            "response_model": response_model,
            "messages": messages,
        }

        if self.provider == LLMProvider.OPENAI:
            if functions:
                completion_params["functions"] = functions
            if function_call:
                completion_params["function_call"] = function_call

        return self.client.chat.completions.create(**completion_params)
