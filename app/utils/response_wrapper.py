# app/utils/response_wrapper.py

def api_response(data=None, message="Success", status=True, error=None):
    return {
        "status": status,
        "message": message,
        "data": data,
        "error": error,
    }
