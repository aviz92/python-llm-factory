from pydantic import BaseModel, Field

from python_llm_factory import LLMFactory
from python_llm_factory.config.settings import Settings

if __name__ == "__main__":

    class CompletionModel(BaseModel):
        response: str = Field(description="Your response to the user.")
        reasoning: str = Field(description="Explain your reasoning for the response.")

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "If it takes 2 hours to dry 1 shirt out in the sun, how long will it take to dry 5 shirts?",
        },
    ]

    llm = LLMFactory(
        settings=Settings().gemini.gemini_2_5_flash,
    )
    completion = llm.completions_create(
        response_model=CompletionModel,
        messages=messages,
    )
    assert isinstance(completion, CompletionModel)

    print(f"Response: {completion.response}\n")
    print(f"Reasoning: {completion.reasoning}")
