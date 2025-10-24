def get_weather(city: str) -> dict:
    temperature_c = 25.0  # Dummy temperature value
    return {
        "city": city,
        "temperature_c": temperature_c,
        "unit": "Celsius",
    }


function_descriptions = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a given city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city to get the weather for.",
                },
            },
            "required": ["city"],
        },
    },
}
