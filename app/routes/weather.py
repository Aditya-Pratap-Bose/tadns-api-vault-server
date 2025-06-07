from flask import Blueprint, jsonify
from app.utils.api_helpers import get_weather
from app.core.auth_middleware import check_auth

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/weather/<city>")
def weather_route(city):
    auth = check_auth()
    if auth:
        return auth

    data = get_weather(city)
    return jsonify({"status": "success",
                    "results": data})
