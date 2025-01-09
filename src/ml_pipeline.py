import os
from read_data import DataIngestor
from preprocess_text import DataPreprocessor
from train_test_split import TrainTestSplitter


class Pipeline:
    def __init__(self):
        self.dg = DataIngestor(os.path.dirname(os.getcwd()), 'raw_data\\IMDB Dataset.csv')

    def run(self):
        df_reviews = self.dg.read_data()

        dp = DataPreprocessor(df_reviews)
        df_reviews = dp.fix_all_data(col='review')

        ts = TrainTestSplitter(df_reviews)
        X_train,X_test,y_train,y_test  = ts.prepare_data()
        print(X_train)