def format_message(event_type, payload):
    if event_type == "stream_live":
        channel = payload.get("channel", "channel")
        return f"{channel} is live."
    if event_type == "new_follower":
        follower = payload.get("follower", "unknown")
        return f"New follower: {follower}."
    return "New event received."
