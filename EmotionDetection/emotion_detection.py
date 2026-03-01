"""
Emotion Detection module using Watson NLP EmotionPredict API.
"""

import requests


def emotion_detector(text_to_analyze):
    """
    Analyze the input text and return detected emotions and dominant emotion.
    """

    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code != 200:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        result_json = response.json()

        # ✅ Correct extraction
        emotion_data = result_json["emotionPredictions"][0]["emotion"]

        emotions = {
            "anger": emotion_data["anger"],
            "disgust": emotion_data["disgust"],
            "fear": emotion_data["fear"],
            "joy": emotion_data["joy"],
            "sadness": emotion_data["sadness"]
        }

        dominant_emotion = max(emotions, key=emotions.get)
        emotions["dominant_emotion"] = dominant_emotion

        return emotions

    except Exception:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
