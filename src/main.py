import os
from read_data import DataIngestor

dg = DataIngestor(os.path.dirname(os.getcwd()), 'raw_data\\IMDB Dataset.csv')
df = dg.read_data()
print(df.head(10))