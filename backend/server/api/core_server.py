from dotenv import load_dotenv
from flask import Flask, Response, request

from .model_api import model_blueprint
def create_core_server(config=None):
    """
    Creates and returns a Flask app that interfaces
    between the frontend sending image screenshots
    and an ML model that takes those screenshots and processes them
    """

    load_dotenv()

    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(model_blueprint)

