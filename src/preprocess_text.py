import re
import string
from textblob import TextBlob
from nltk.corpus import stopwords
import nltk

class DataPreprocessor:
    def __init__(self, df):
        self.df = df
        self.punctuation = string.punctuation
        nltk.download('stopwords')

    def make_lower_case(self, col):
        self.df[col] = self.df[col].str.lower()

    @staticmethod
    def handle_html_tags(text):
        pattern = re.compile('<.*?>')
        return pattern.sub(r'', text)

    @staticmethod
    def remove_url(text):
        pattern = re.compile(r'https?://\S+|www\.\S+')
        return pattern.sub(r'', text)

    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', self.punctuation))

    def fix_typos(self, text):
        textBlb = TextBlob(text)
        return textBlb.correct().string

    @staticmethod
    def remove_stopwords(text):
        new_text = []
        for word in text.split():
            if word in stopwords.words('english'):
                new_text.append('')
            else:
                new_text.append(word)
        x = new_text[:]
        new_text.clear()
        return " ".join(x)

    def fix_all_data(self, col):
        self.make_lower_case(col)
        self.df[col] = self.df[col].apply(self.handle_html_tags)
        self.df[col] = self.df[col].apply(self.remove_url)
        self.df[col] = self.df[col].apply(self.remove_punctuation)
        return self.df
