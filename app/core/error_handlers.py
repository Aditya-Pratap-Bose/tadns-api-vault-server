# app/core/error_handlers.py

from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            "error": "Route not found",
            "status": 404
        }), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({
            "error": "Internal server error",
            "status": 500
        }), 500
