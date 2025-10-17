from custom_python_logger import json_pretty_format


def log_kwargs(**kwargs):
    print(f"Function called with kwargs: {json_pretty_format(kwargs)}")

def add_logging_hooks(client):
    client.client.on("completion:kwargs", log_kwargs)
