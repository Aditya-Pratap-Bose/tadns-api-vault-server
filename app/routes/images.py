from flask import Blueprint, jsonify
from app.utils.api_helpers import get_unsplash_images, get_pixabay_images
from app.core.auth_middleware import check_auth

images_bp = Blueprint("images", __name__)


@images_bp.route("/search/<api>/images/<query>")
def image_search(api, query):
    auth = check_auth()
    if auth:  # unauthorized
        return auth

    if api == "unsplash":
        data = get_unsplash_images(query)
    elif api == "pixabay":
        data = get_pixabay_images(query)
    else:
        return jsonify({"error": f"API '{api}' not supported"}), 400

    return jsonify({"status": "success",
                    "source": api,
                    "results": data})
