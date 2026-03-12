import requests
import json

def emotion_detector(text_to_analyse):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=input_json, headers=headers)

    response_dict = json.loads(response.text)

    emotions = response_dict["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
if __name__ == "__main__":
    print(emotion_detector("I love this new technology."))
