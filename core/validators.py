def validate_event(data):
    amount = data.get("amount")
    event_type = data.get("type")

    if amount is None or amount <= 0:
        raise ValueError("Amount must be greater than 0")

    if event_type not in ["income", "expense"]:
        raise ValueError("Invalid event type")

    if not data.get("category"):
        raise ValueError("Category is required")

    if not data.get("date"):
        raise ValueError("Date is required")