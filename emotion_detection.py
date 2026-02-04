""" module d'analyse d'une emotion """

import json
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    """ Url a appeller"""
    https = 'https://sn-watson-emotion.labs.skills.network/'
    route = 'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    url = https + route

    myobj = { "raw_document": { "text": text_to_analyse } }
    myheader = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(
            url,
            json=myobj,
            headers=myheader,
            timeout=(3, 10)
        )
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("⏱️ Timeout atteint")
    except requests.exceptions.RequestException as e:
        print("❌ Erreur HTTP:", e)

    return response.text
