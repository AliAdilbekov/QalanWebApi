def message_exists(messages: list, expected_text: str) -> bool:
    return any(m.get("text") == expected_text for m in messages)
