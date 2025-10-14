def notify_slack(message: str) -> dict:
    print("Sending Slack message:", message)
    return {"status": "sent", "message": message}
