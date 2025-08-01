import os
import json
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL = "j-hartmann/emotion-english-distilroberta-base"


def emotion_detector(text_to_analyze):
    client = InferenceClient(
        provider="hf-inference",
        api_key=HF_TOKEN,
    )

    results = client.text_classification(
        text_to_analyze,
        model=MODEL,
    )

    emotion_dict = {result["label"]: result["score"] for result in results}
    # list has dmoinant emotion at top so....
    emotion_dict["dominant_emotion"] = list(emotion_dict.keys())[0]
    return emotion_dict

