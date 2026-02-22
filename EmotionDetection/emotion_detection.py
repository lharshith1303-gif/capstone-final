import requests, json

def emotion_detector(text_to_analyze):
    '''
    This function is to understand the emotion that we got from a phrase that we pass as a argument
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    body = { 'raw_document': { 'text': text_to_analyze } }
    response = requests.post(url, json = body, headers=header)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        analysis_result = response_json['emotionPredictions'][0]['emotion']
        analysis_result['dominant_emotion'] = max(analysis_result, key=analysis_result.get)
        return analysis_result
    elif response.status_code == 400:
        return {'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 0, 'sadness': 0, 'dominant_emotion': None}
    