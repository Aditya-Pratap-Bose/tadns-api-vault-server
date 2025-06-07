import os
import json
import time
from hashlib import md5

# Folder to store cache files
CACHE_DIR = os.path.join(os.path.dirname(__file__), '../../cache/')
os.makedirs(CACHE_DIR, exist_ok=True)

# Set expiry in seconds (default = 10 mins)
CACHE_EXPIRY_SECONDS = 600

#  Generate safe filename using hash
def get_cache_filename(api_name, media_type, query):
    key = f"{api_name}_{media_type}_{query}".lower()
    hashed = md5(key.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f"{hashed}.json")

#  Load from cache if exists + not expired
def load_from_cache(api_name, media_type, query, force=False):
    if force:
        return None  # force to skip cache

    path = get_cache_filename(api_name, media_type, query)
    if not os.path.exists(path):
        return None

    with open(path, 'r') as f:
        try:
            content = json.load(f)
        except json.JSONDecodeError:
            return None

    timestamp = content.get("timestamp", 0)
    if time.time() - timestamp > CACHE_EXPIRY_SECONDS:
        return None

    return content.get("data")


#  Save new API result to cache
def save_to_cache(api_name, media_type, query, data):
    path = get_cache_filename(api_name, media_type, query)
    with open(path, 'w') as f:
        json.dump({
            "timestamp": time.time(),
            "data": data
        }, f)
