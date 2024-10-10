from flask import Flask
from dotenv import load_dotenv
import os 

load_dotenv()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    from .main import app_routes
    app.register_blueprint(app_routes)
    return app
     