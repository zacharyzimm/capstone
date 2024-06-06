import os
import requests
from PIL import Image
from io import BytesIO
import cv2

class ModelConnection:
    def __init__(self):
        pass

    def checkout(self):
        pass

    def predict(self):
        pass

class ModelClient:
    """
    Client that talks to the model deployment and returns a response
    """
    def __init__(self, image_url):
        self.image_url = image_url
        self.image = self.download_and_preprocess_image()

        # use a shared model connection since ModelClient is instantiated for
        # each API call, thus preventing opening too many unnecessary connections

        if ModelClient.model_connection is None:
            ModelClient.model_connection = ModelConnection()

        self.model_connection = ModelClient.model_connection.checkout()

    def download_and_preprocess_image(self):
        """
        Download the static image from the Google Maps Static API
        and preprocess it to send to the model
        """
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
        """
        Send the preprocessed image to the model
        and get a response back
        """
        annotated_image = self.model_connection.predict(self.image)
        return annotated_image

    def predict(self):
        try:
            image = self.send_image_to_model()
            return image

        except:
            raise Exception
        # TODO: fill out exception handling

