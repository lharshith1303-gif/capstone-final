"""
    This module sends a request to a 
    cloud library and receives the response.
"""
# Import the requests library to handle HTTP requests.
import requests
# Imports JSON library for text formatting.
import json

def emotion_detector(text_to_analyse):
    
    ''' Define a function that receives a string 
        as input (text_to_analyze) and returns a 
        JSON object with selected information 
        from the API response objects.
    '''

    # URL for the emotion analysis service
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService"
        "/EmotionPredict"
    )

    # Defines the headers required for the API request.
    header = {
        "grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Create a dictionary with the text to be analyzed.
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Send a POST request to the API with the text and headers.
    response = requests.post(url, json = myobj, 
                            headers=header, timeout = (2, 10))

    # It performs the parsing and converts 
    # the data into a dictionary to make it easier to work with.
    formatted = json.loads(response.text)

    # Creates an empty dictionary to 
    # assign the selected values ​​later.
    formatted_out = dict()

    if response.status_code == 200:  

        # Search the JSON response, assigning only the key 
        # "emotion" and its score to the new dictionary.
        for (formatted, 
            score) in formatted['emotionPredictions'][0]['emotion'].items():

            formatted_out.update({f"{formatted}" : f"{score}"})
        
        # Identifies the key with the highest score and adds 
        # the new key with the highest-scoring emotion as its value.
        formatted_out.update({"dominant_emotion" :
            f"{max(formatted_out, key = formatted_out.get)}"})
    
    elif response.status_code == 400:
    
        formatted_out = {
        'anger': None, 
        'disgust': None, 
        'fear': None, 
        'joy': None, 
        'sadness': None,
        'dominant_emotion': None 
        }
    
    return formatted_out
