def success_response(data, message="OK"):
    return {
        "success": True,
        "data": data,
        "message": message
    }

def error_response(type, message, details=None):
    return {
        "error": {
            "type": type,
            "message": message,
            "details": details
        }
    }