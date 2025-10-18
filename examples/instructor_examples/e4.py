from custom_python_logger import build_logger
from pydantic import BaseModel

from examples.instructor_examples.create_gemini_client import create_default_client
from python_llm_factory.config.settings import set_logging_level
from python_llm_factory.hooks.logging_hooks import add_logging_hooks, log_kwargs


class UserInfo(BaseModel):
    name: str
    age: int


if __name__ == "__main__":
    logger = build_logger(__name__)

    client = create_default_client()
    set_logging_level()

    add_logging_hooks(client=client, handler=log_kwargs)

    user_info = client.completions_create(
        response_model=UserInfo,
        messages=[{"role": "user", "content": "Extract the user name: 'John is 20 years old'"}],
    )

    """
    {
            'args': (),
            'kwargs': {
                'messages': [
                    {
                        'role': 'user',
                        'content': "Extract the user name: 'John is 20 years old'",
                    }
                ],
                'tools': [
                    {
                        'type': 'function',
                        'function': {
                            'name': 'UserInfo',
                            'description': 'Correctly extracted `UserInfo` with all the required parameters with
                            correct types',
                            'parameters': {
                                'properties': {
                                    'name': {'title': 'Name', 'type': 'string'},
                                    'age': {'title': 'Age', 'type': 'integer'},
                                },
                                'required': ['age', 'name'],
                                'type': 'object',
                            },
                        },
                    }
                ],
                'tool_choice': {'type': 'function', 'function': {'name': 'UserInfo'}},
            },
        }
    """

    print(f"Name: {user_info.name}, Age: {user_info.age}")  # > Name: John, Age: 20
