from flask import Blueprint, request
from ..clients import ModelClient


model_blueprint = Blueprint("model", __name__, url_prefix="/model-api")

@model_blueprint.route("/model-response", methods=["GET"])
def get_current_model_response():
    pass

@model_blueprint.route("/predict", methods=["POST"])
def fetch_model_response():
    image_url = request.args.get("image_url")
    model_client = ModelClient(image_url)

    model_client.predict()




