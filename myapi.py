import json
import requests
from dotenv import load_dotenv
import os

class API:

    def __init__(self):
        load_dotenv()
        self.headers = {"Authorization": os.getenv("API_KEY")}

    def sentiment_analysis(self, text):
        url = "https://api.edenai.run/v2/text/sentiment_analysis"
        payload = {
            "providers": "google,amazon",
            "language": "en",
            "text": text,
        }

        response = requests.post(url, json=payload, headers=self.headers)

        result = json.loads(response.text)
        return result['google']['items']
    
    def ner(self, text):
        url = "https://api.edenai.run/v2/text/named_entity_recognition"
        payload = {
            "providers": "google,amazon",
            "language": "en",
            "text": text,
        }

        response = requests.post(url, json=payload, headers=self.headers)

        result = json.loads(response.text)
        return result['amazon']['items']
    
    def emotion_analysis(self, text):
        url = "https://api.edenai.run/v2/text/emotion_detection"
        payload = {
            "providers": "nlpcloud,vernai",
            "text": text,
        }

        response = requests.post(url, json=payload, headers=self.headers)

        result = json.loads(response.text)
        return result["nlpcloud"]["items"]