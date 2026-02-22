''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
@app.route("/emotionDetector")
def sent_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions value
        and the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    result = (f"For the given statement, the system response is "
              f"'anger': {response['anger']}, "
              f"'disgust': {response['disgust']}, "
              f"'fear': {response['fear']}, "
              f"'joy': {response['joy']} and "
              f"'sadness': {response['sadness']}. "
              f"The dominant emotion is {response['dominant_emotion']}.")
    return result
