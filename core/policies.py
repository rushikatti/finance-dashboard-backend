def can_access(user, action):
    # inactive users cannot perform any action
    if user.status != "active":
        return False

    if user.role == "admin":
        return True

    if user.role == "analyst":
        return action in [
            "VIEW_EVENTS",
            "VIEW_DASHBOARD"
        ]

    if user.role == "viewer":
        return action == "VIEW_DASHBOARD"

    return False