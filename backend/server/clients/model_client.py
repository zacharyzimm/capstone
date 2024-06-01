import os
import requests


class ModelClient:
    """
    Client that talks to the model deployment and returns a response
    """

    def __init__(self):
        self.google_maps_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
        self.bing_maps_api_key = os.environ.get("BING_MAPS_API_KEY")

    def talk_to_model(self):
        pass

    def process_image(self):
        image = self.talk_to_model()
        return image

    def annotate_image(self):

    def get_response(self):
        image = self.process_image()
        annotated_image = self.annotate_image()
        return annotated_image