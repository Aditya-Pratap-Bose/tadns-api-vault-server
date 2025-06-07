# app/utils/clean_cache.py

import os
import json
import time

CACHE_DIR = "./cache"
EXPIRY_SECONDS = 600  # Same as your main cache logic

def clean_expired_cache():
    if not os.path.exists(CACHE_DIR):
        return

    for filename in os.listdir(CACHE_DIR):
        if not filename.endswith(".json"):
            continue

        path = os.path.join(CACHE_DIR, filename)

        try:
            with open(path, "r") as f:
                data = json.load(f)
            ts = data.get("timestamp", 0)
        except Exception:
            continue

        if time.time() - ts > EXPIRY_SECONDS:
            try:
                os.remove(path)
            except Exception:
                pass
