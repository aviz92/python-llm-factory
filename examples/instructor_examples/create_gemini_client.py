from python_llm_factory import LlmInstructorFactory
from python_llm_factory.config.settings import Settings


def create_default_client() -> LlmInstructorFactory:
    return LlmInstructorFactory(
        settings=Settings().gemini.gemini_2_5_flash,
    )
