# app/routes/ui.py

from flask import Blueprint, request, render_template
from app.utils.api_helpers import (
    get_unsplash_images,
    get_pixabay_images,
    get_pixabay_videos,
)

ui_bp = Blueprint("ui", __name__)

@ui_bp.route("/")
def test_ui():
    query = request.args.get("query")
    api = request.args.get("api")
    media = request.args.get("media")
    results = None

    if query and api and media:
        if media == "images":
            if api == "unsplash":
                results = get_unsplash_images(query)
            elif api == "pixabay":
                results = get_pixabay_images(query)
        elif media == "videos" and api == "pixabay":
            results = get_pixabay_videos(query)

    return render_template("index.html", results=results, media=media)
