import requests  # Import the requests library to handle HTTP requests
import json 

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }  

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)  

    # If the response status code is 200, emotions and find domninant emotion
    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
        
        # Extracting emotions from the response
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        # Finding the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

    # If the response status code is 400, set emotions and domninant emotion to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # Creating dictionary containing emotion detector results
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    # Return dictionary containing emotion detector results
    return result