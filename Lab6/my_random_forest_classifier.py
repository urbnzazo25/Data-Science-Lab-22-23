import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from scipy import stats


class MyRandomForestClassifier():
    def __init__(self, n_estimators: int, max_features: str):
        self.trees = [ DecisionTreeClassifier(splitter='random', max_features=max_features) for _ in range(0, n_estimators) ]

    def fit(self, X: pd.DataFrame, y: pd.DataFrame):
        for tree in self.trees:
            X1, y1 = self.__select_random_rows(X, y)
            tree.fit(X1, y1)

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        i = 0
        for tree in self.trees:
            y = tree.predict(X)
            if i == 0:
                y_pred = y.reshape(1, -1)
            else:
                y_pred = np.append(y_pred, y.reshape(1, -1), axis=0)
            i += 1
        return stats.mode(y_pred, axis=0, nan_policy='omit', keepdims=False)[0]


    def __select_random_rows(self, X: pd.DataFrame, y: pd.DataFrame) -> tuple:
        n_rows = X.shape[0]
        idx = np.random.choice(n_rows, size=n_rows, replace=True)
        return X.iloc[idx, :], y.iloc[idx]