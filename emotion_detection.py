#from flask import Flask
import json
import requests

URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
TEST_STRING = "I love this technology."

def emotion_detector(text_to_analyze:str):
    payload = { "raw_document": { "text": text_to_analyze}}
    response = requests.post(
        url=URL, 
        headers=Headers, 
        data=json.dumps(payload), 
        timeout=30
    )

    # Check for errors
    if response.status_code == 200:
        data = response.json()["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(data, key=data.get)        
        data['dominant_emotion'] = dominant_emotion
        print(json.dumps(data,indent=4))