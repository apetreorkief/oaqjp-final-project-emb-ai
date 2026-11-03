import json

import requests


def emotion_detector(text_to_analyze):
    """Return the five emotion scores and the dominant emotion for the given text."""
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers, timeout=10)
    formatted = json.loads(response.text)
    emotions = formatted["emotionPredictions"][0]["emotion"]

    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    result["dominant_emotion"] = max(emotions, key=emotions.get)
    return result
