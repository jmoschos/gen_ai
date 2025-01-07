import pandas as pd
import re

class DataPreprocessor:
    def __init__(self, df):
        self.df = df

    def make_lower_case(self, col):
        self.df[col] = self.df[col].str.lower()

    def handle_html_tags(self, text):
        pattern = re.compile('<.*?>')
        return pattern.sub(r'', text)

    def fix_all_data(self, col):
        self.make_lower_case(col)
        self.df[col] = self.df[col].apply(self.handle_html_tags)
        return self.df
