import pandas as pd

class DataIngestor:
    def __init__(self, base_path, file_name):
        self.base_path = base_path
        self.file_name = file_name

    def read_data(self):
        self.df = pd.read_csv(self.base_path + '\\' + self.file_name)
        return self.df

