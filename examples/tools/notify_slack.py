def notify_slack(message: str) -> dict:
    print("Sending Slack message:", message)
    return {"status": "sent", "message": message}


function_descriptions = {  # pylint: disable=R6101
    "notify_slack": {
        "name": "notify_slack",
        "description": "Sends a Slack message with the given content.",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "The content of the Slack message to be sent.",
                },
            },
            "required": ["message"],
        },
    },
}
