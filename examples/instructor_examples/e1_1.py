from pydantic import BaseModel

from examples.instructor_examples.create_gemini_client import create_default_client

client = create_default_client()


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class Person(BaseModel):
    name: str
    age: int
    addresses: list[Address]


###

person = client.completions_create(
    response_model=Person,
    messages=[
        {
            "role": "user",
            "content": "Extract a detailed person profile for John Smith, 35, who lives in Chicago and Springfield.",
        }
    ],
)
print("response 1:")
print(person)
print()

###

# Stream the response as it's being generated
stream = client.client.chat.completions.create_partial(
    model="gemini-2.5-flash",
    response_model=Person,
    messages=[
        {
            "role": "user",
            "content": "Extract a detailed person profile for John Smith, 35, who lives in Chicago and Springfield.",
        }
    ],
)

print("response 2:")
for partial in stream:
    # This will incrementally show the response being built
    print(partial)
