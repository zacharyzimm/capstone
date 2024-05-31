import os
import json
from flask import Flask, abort, request

MOCK_RESPONSE_DIR = "./data/"

def create_mock_server():
    """
    Creates and returns a server that returns mock model outputs
    for app development testing
    """
    mock_server = Flask(__name__)

    def get_json(filepath):
        if not os.path.exists(filepath):
            abort(404)
        else:
            json.load(filepath)

    @mock_server.route("/map", methods=["GET"]):
    def get_map():
        """
        Accesses the Google API endpoint and brings up a map
        """
        pass
    @mock_server.route("/generate-image", methods=["POST"]):
    def generate_image():
        """
        Takes the currently displayed map and generates an image
        """
        pass
    @mock_server.route("/model-response", methods=["GET", "POST"]):
    def get_model_response():
        """
        Sends a generated image to the ML model and fetches a response
        """
        pass