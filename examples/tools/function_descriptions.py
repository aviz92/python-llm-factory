function_descriptions = {  # pylint: disable=R6101
    "create_jira_bug": {
        "name": "create_jira_bug",
        "description": "Creates a new Jira bug with the given title.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The title of the Jira bug to be created.",
                },
            },
            "required": ["title"],
        },
    },
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
