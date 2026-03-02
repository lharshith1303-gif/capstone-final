'''
function to run emotion detection using the appropriate Emotion Detection function
'''
import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    formatted_response = json.loads(response.text)
    if response.status_code == 400:
        emotions={'anger': None, 'disgust': None,\
        'fear': None, 'joy': None, 'sadness': None,\
        'dominant_emotion': None}
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        emotions["dominant_emotion"] = dominant_emotion
    return emotions