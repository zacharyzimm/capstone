from flask import Blueprint, Request


model_blueprint = Blueprint("model", __name__, url_prefix="/model_api")

@model_blueprint.route("/model-response", methods=["GET"])
def get_current_model_response():
    pass

@model_blueprint.route("/model-response", methods=["POST"])
def fetch_model_response():
    pass

