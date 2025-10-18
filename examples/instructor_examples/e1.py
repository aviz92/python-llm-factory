from pydantic import BaseModel

from examples.instructor_examples.create_gemini_client import create_default_client


class Person(BaseModel):
    name: str
    age: int
    occupation: str


if __name__ == "__main__":
    client = create_default_client()
    person = client.completions_create(
        response_model=Person,
        messages=[{"role": "user", "content": "Extract: John is a 30-year-old software engineer"}],
    )
    print(person)  # Person(name='John', age=30, occupation='software engineer')
