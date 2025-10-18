from pydantic import BaseModel

from examples.instructor_examples.create_gemini_client import create_default_client
from python_llm_factory.tools.weather import function_descriptions


class Weather(BaseModel):
    city: str
    temperature_c: float
    unit: str


if __name__ == '__main__':
    client = create_default_client()

    response_list = []
    messages = [
        {"role": "system", "content": "You are a helpful weather assistant."},
        {"role": "user", "content": "What's the weather in Tel Aviv?"}
    ]
    res = client.completions_tools(
        messages=messages,
        response_format=Weather,
        tools=function_descriptions,
        tool_choice={"type": "function", "function": {"name": "get_weather"}},
    )
    print(res.choices[0].message.parsed.model_dump_json(indent=2))
