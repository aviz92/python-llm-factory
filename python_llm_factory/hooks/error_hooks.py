def log_exception(exception: Exception):
    print(f"An exception occurred: {str(exception)}")


def add_error_hooks(client):
    client.client.on("completion:error", log_exception)
