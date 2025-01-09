from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class TrainTestSplitter:
    def __init__(self, df, test_size=0.2):
        self.df = df
        self.X = df['review']
        self.y = df['sentiment']
        self.test_size = test_size

    def encode_labels(self):
        encoder = LabelEncoder()
        self.y = encoder.fit_transform(self.y)

    def split(self):
        X_train,X_test,y_train,y_test = train_test_split(self.X,self.y,test_size=self.test_size,random_state=42)
        return X_train,X_test,y_train,y_test

    def prepare_data(self):
        self.encode_labels()
        X_train,X_test,y_train,y_test  = self.split()
        return X_train,X_test,y_train,y_test