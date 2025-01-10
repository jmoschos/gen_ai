from transformers import pipeline

class Solution:
    def __init__(self):
        classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device=0)
        text = 'it was average at best'

        result = classifier(text)
        print(result, text)