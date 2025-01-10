from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification


class Solution:
    def __init__(self, model_name='nlptown/bert-base-multilingual-uncased-sentiment', device=0):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.classifier = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer, device=device)

    def get_sentiment(self, text):
        """
        Analyze sentiment for a given text or a list of texts.

        Args:
            text (str or list): Text or list of texts to analyze.

        Returns:
            list: List of sentiment analysis results.
        """
        if isinstance(text, str):
            text = [text]  # Convert single string to a list for uniform processing
        result = self.classifier(text)
        return result

    @classmethod
    def with_default_model(cls):
        """
        Quick setup with the default model.

        Returns:
            Solution: An instance of Solution preconfigured with the default model.
        """
        return cls()
