import requests
import json

def emotion_detector(text_to_analyse):
    """
    Detects emotions from input text using Watson NLP Emotion Predict function.
    
    Args:
        text_to_analyse (str): Text to analyze for emotions
        
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion
    """
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check for status code 400 (bad request/blank entry) FIRST
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Convert response text to dictionary
        formatted_response = json.loads(response.text)
        
        # Extract emotions from the response
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Extract individual emotion scores
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        # Find the dominant emotion (highest score)
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return in the required format
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    # For any other status code, return None values
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
