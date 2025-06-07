# app/utils/api_helpers.py

import os
import requests
from flask import current_app, request
from app.utils.cache_helper import load_from_cache, save_to_cache

# UNSPLASH IMAGE SEARCH
def get_unsplash_images(query):
    force = request.args.get("force", "false").lower() == "true"

    # 1. Try from cache
    cached = load_from_cache("unsplash", "images", query, force=force)
    if cached:
        return cached

    # 2. Hit API
    key = current_app.config.get("UNSPLASH_ACCESS_KEY")
    url = f"https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "client_id": key,
        "per_page": 10
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return {"error": "Failed to fetch from Unsplash"}

    data = response.json()
    results = [{
        "id": img["id"],
        "desc": img.get("description") or img.get("alt_description"),
        "url": img["urls"]["regular"]
    } for img in data.get("results", [])]

    # 3. Save to cache
    save_to_cache("unsplash", "images", query, results)
    return results


# PIXABAY IMAGE SEARCH
def get_pixabay_images(query):
    force = request.args.get("force", "false").lower() == "true"

    cached = load_from_cache("pixabay", "images", query, force=force)
    if cached:
        return cached

    key = current_app.config.get("PIXABAY_API_KEY")
    url = "https://pixabay.com/api/"
    params = {
        "key": key,
        "q": query,
        "image_type": "photo",
        "per_page": 10
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return {"error": "Failed to fetch from Pixabay"}

    data = response.json()
    results = [{
        "id": img["id"],
        "tags": img["tags"],
        "url": img["webformatURL"]
    } for img in data.get("hits", [])]

    save_to_cache("pixabay", "images", query, results)
    return results


# PIXABAY VIDEO SEARCH
def get_pixabay_videos(query):
    force = request.args.get("force", "false").lower() == "true"

    cached = load_from_cache("pixabay", "videos", query, force=force)
    if cached:
        return cached

    key = current_app.config.get("PIXABAY_API_KEY")
    url = "https://pixabay.com/api/videos/"
    params = {
        "key": key,
        "q": query,
        "per_page": 10
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return {"error": "Failed to fetch video from Pixabay"}

    data = response.json()
    results = [{
        "id": video["id"],
        "tags": video["tags"],
        "url": video["videos"]["medium"]["url"]
    } for video in data.get("hits", [])]

    save_to_cache("pixabay", "videos", query, results)
    return results


# WEATHER SEARCH (No caching)
def get_weather(city):
    key = current_app.config.get("OPENWEATHER_API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "APPID": key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {
            "error": f"Weather not found for '{city}'",
        }

    data = response.json()

    return {
        "city": data.get("name"),
        "desc": data["weather"][0]["description"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "visibility": data.get("visibility"),
        "sunrise": data["sys"]["sunrise"],
        "sunset": data["sys"]["sunset"],
        "timestamp": data.get("dt")
    }
