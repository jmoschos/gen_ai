from sklearn.metrics import accuracy_score,confusion_matrix

class ModelEvaluator:
    def __init__(self, predictions, y_test):
        self.predictions = predictions
        self.y_test = y_test

    def evaluate_accuracy(self):
        return accuracy_score(self.predictions, self.y_test)