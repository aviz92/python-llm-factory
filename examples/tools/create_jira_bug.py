def create_jira_bug(title: str) -> dict:
    return {"bug_id": "JIRA-1234", "title": title}


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
}
