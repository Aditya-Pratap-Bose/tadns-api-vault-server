# app/core/auth_middleware.py
from flask import request, jsonify, current_app


def check_auth():
    """Abort the request if X-Api-Secret header is missing / wrong."""
    required = current_app.config.get("BACKEND_SECRET_KEY")
    incoming = request.headers.get("X-Api-Secret")

    if incoming != required:
        return jsonify({"error": "Unauthorized",
                        "status": 401}), 401
    # else return None -> caller continues
