# app/config.py
import os
from dotenv import load_dotenv

# .env file load karo
load_dotenv()

class Config:
    SHOW_UI = os.getenv("SHOW_UI", "false").lower() == "true"
    BACKEND_SECRET_KEY = os.getenv("BACKEND_SECRET_KEY")
    PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")
    UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
