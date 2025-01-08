import os
from read_data import DataIngestor
from preprocess_text import DataPreprocessor

dg = DataIngestor(os.path.dirname(os.getcwd()), 'raw_data\\IMDB Dataset.csv')
df_reviews = dg.read_data()

dp = DataPreprocessor(df_reviews)
df_new = dp.fix_all_data(col='review')
print(df_new.head(10))