from examples.instructor_examples.create_gemini_client import create_default_client

client = create_default_client()

response = client.completions_create(
    response_model=None,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short poem about the moon."},
    ],
    temperature=0.8,
)

print(response.choices[0].message.content)
