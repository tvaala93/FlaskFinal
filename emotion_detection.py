#from flask import Flask
import json
import requests

URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

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
        data = response.json()
        print(data)