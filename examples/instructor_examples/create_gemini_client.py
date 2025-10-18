from python_llm_factory import LLMFactory
from python_llm_factory.config.settings import Settings


def create_default_client() -> LLMFactory:
    return LLMFactory(
        settings=Settings().gemini.gemini_2_5_flash,
    )
