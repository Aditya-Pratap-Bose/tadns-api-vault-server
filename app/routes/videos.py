from flask import Blueprint, jsonify
from app.utils.api_helpers import get_pixabay_videos
from app.core.auth_middleware import check_auth

videos_bp = Blueprint("videos", __name__)


@videos_bp.route("/search/pixabay/videos/<query>")
def video_search(query):
    auth = check_auth()
    if auth:
        return auth

    data = get_pixabay_videos(query)
    return jsonify({"status": "success",
                    "source": "pixabay",
                    "results": data})
