import numpy as np


class NullClassifier:
    def fit(self, X, y):
        pass

    def predict(self, X):
        return np.zeros(X.shape[0])
