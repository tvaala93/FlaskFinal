from flask import Flask, jsonify, request, render_template, url_for, redirect
import requests
from EmotionDetection import emotion_detection as ED

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "Hello World!"


@app.route('/emotionDetector', methods=['GET'])
def get_emotion():
    text_to_analyze = request.args.get('textToAnalyze', '')
    #if not text_to_analyze:
    #    return render_template('index.html')

    analysis = ED.emotion_detector(text_to_analyze)
    if analysis['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    output = f"For the given statement, the system response is "
    output += f"'anger': {analysis['anger']}, "
    output += f"'disgust': {analysis['disgust']}, "
    output += f"'fear': {analysis['fear']}, "
    output += f"'joy': {analysis['joy']}, "
    output += f"and 'sadness': {analysis['sadness']}."
    output += f" The dominant emotion is {analysis['dominant_emotion']}."    
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
