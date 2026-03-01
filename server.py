"""Flask web application for Emotion Detection using Watson NLP."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Render the home page with the input form."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze text and return the emotion response.

    Returns a formatted string showing each emotion's score and
    the dominant emotion, or an error message for blank input.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result is None or result["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
