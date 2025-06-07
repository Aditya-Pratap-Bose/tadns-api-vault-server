# app/__init__.py

from flask import Flask
from .config import Config
from .core.error_handlers import register_error_handlers
from app.utils.clean_cache import clean_expired_cache



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Clean old cache files at startup
    clean_expired_cache()

    # Register routes
    from .routes.images import images_bp
    from .routes.videos import videos_bp
    from .routes.weather import weather_bp
    from .routes.ui import ui_bp

    app.register_blueprint(images_bp)
    app.register_blueprint(videos_bp)
    app.register_blueprint(weather_bp)
    app.register_blueprint(ui_bp)



    return app
