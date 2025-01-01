from flask import Flask
from config.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from app.routes import api_bp
    app.register_blueprint(api_bp)
    
    return app

