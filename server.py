''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector


# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():

    ''' This function initiates the rendering of the 
        main application page over the Flask channel
    '''

    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detector():
    '''The endpoint receives information from the front end 
        and sends it to the Emotion_detector method, 
        which receives and organizes the information.
    '''
    # Recupera o texto a ser analisado dos argumentos da requisição
    text_to_analyze = request.args.get("textToAnalyze", type = str)

    # Passa o texto para a função
    # emotion_detector e armazena a resposta
    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!."

    return (
        "For the given statement, the system response " +
        f"'anger': {response.get('anger')}, " +
        f"'disgust': {response.get('disgust')}, " +
        f"'fear': {response.get('fear')}, " +
        f"'joy': {response.get('joy')} and " +
        f"'sadness': {response.get('sadness')}. " +
        f"The dominant emotion is {response.get('dominant_emotion')}. "
    )

if __name__ == "__main__":

    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host = "0.0.0.0", port = 5000)
    # End-of-file (EOF)
