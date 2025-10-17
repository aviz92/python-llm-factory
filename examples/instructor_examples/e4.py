from pydantic import BaseModel

from examples.instructor_examples.create_gemini_client import create_default_client
from python_llm_factory.hooks.error_hooks import add_error_hooks
from python_llm_factory.hooks.logging_hooks import add_logging_hooks


class UserInfo(BaseModel):
    name: str
    age: int


if __name__ == '__main__':
    client = create_default_client()

    add_logging_hooks(client=client)
    add_error_hooks(client=client)

    user_info = client.completions_create(
        response_model=UserInfo,
        messages=[
            {"role": "user", "content": "Extract the user name: 'John is 20 years old'"}
        ],
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
                'model': 'gpt-3.5-turbo',
                'tools': [
                    {
                        'type': 'function',
                        'function': {
                            'name': 'UserInfo',
                            'description': 'Correctly extracted `UserInfo` with all the required parameters with correct types',
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

    print(f"Name: {user_info.name}, Age: {user_info.age}")  #> Name: John, Age: 20
