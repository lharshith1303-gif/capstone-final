"""
Flask web server for Emotion Detection application.
Deploys the emotion detector on localhost.
"""

from flask import Flask, render_template, request, jsonify  # pylint: disable=import-error
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main HTML page."""
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_handler():  # pylint: disable=invalid-name
    """
    Analyze text for emotions and return formatted response.
    Expects GET parameter textToAnalyze.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or not str(text_to_analyze).strip():
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    text_to_analyze = str(text_to_analyze).strip()
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    formatted = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({
        'formatted_response': formatted,
        'anger': result['anger'],
        'disgust': result['disgust'],
        'fear': result['fear'],
        'joy': result['joy'],
        'sadness': result['sadness'],
        'dominant_emotion': result['dominant_emotion']
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)