'''
server.py - This module handles the server-side operations using Flask
'''
from flask import Flask, request
from EmotionDetection import emotion_detection as ED

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def get_emotion():
    '''
    This function gets a user input from the web and routes it to the emotion detector.
    The response is then returned to the webpage.
    '''

    text_to_analyze = request.args.get('textToAnalyze', '')

    analysis = ED.emotion_detector(text_to_analyze)
    if analysis['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    output = "For the given statement, the system response is "
    output += f"'anger': {analysis['anger']}, "
    output += f"'disgust': {analysis['disgust']}, "
    output += f"'fear': {analysis['fear']}, "
    output += f"'joy': {analysis['joy']}, "
    output += f"and 'sadness': {analysis['sadness']}."
    output += f" The dominant emotion is {analysis['dominant_emotion']}."
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
