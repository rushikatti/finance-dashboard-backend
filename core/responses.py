def success(data):
    return {
        "status": "success",
        "data": data
    }

def error(code, message):
    return {
        "status": "error",
        "error": code,
        "message": message
    }