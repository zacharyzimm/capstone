import os
import requests
from PIL import Image
from io import BytesIO
import cv2

class ModelClient():
    """
    Client that talks to the model deployment and returns a response
    """

    def __init__(self, image_url):
        self.image_url = image_url
        self.image = self.download_and_preprocess_image()

    def download_and_preprocess_image(self):
        try:
            response = requests.get(self.image_url)
            img = None
            # open image
            # img = Image.open(BytesIO(response.content))
            # img = cv2
            # TODO: image preprocessing goes here
            return img
        except Exception as e:
            raise Exception # TODO: make better exception handling

    def send_image_to_model(self):
        pass

    def predict(self):
        self.send_image_to_model()

