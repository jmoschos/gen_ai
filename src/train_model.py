from sklearn.ensemble import RandomForestClassifier

class ModelTrainer:
    def __init__(self, X_train, y_train, X_test):
        self.rf = RandomForestClassifier()
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test

    def train(self):
        self.rf.fit(self.X_train, self.y_train)

    def predict(self):
        y_pred = self.rf.predict(self.X_test)
        return y_pred

    def train_and_predict(self):
        self.train()
        predictions = self.predict()
        return predictions