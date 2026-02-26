# Define the emotion detection function
# No need to import the Watson NLP Library in the IDE
# The only need is to send a post request to the URL 

# Import necessary libraries
import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {'raw_document': {'text': text_to_analyse}}
    header = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        list_of_emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        dominant_emotion = max(list_of_emotions, key = list_of_emotions.get)
    else:
        list_of_emotions = None
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
        }
