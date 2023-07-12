import numpy as np


class KNearestNeighbors:
    def __init__(self, k: int, distance_metric="euclidean", weights="uniform"):
        self.__k = k
        self.__distance_metric = distance_metric
        self.__weights = weights
        self.__x_train = None
        self.__y_train = None

    def fit(self, x_train: np.ndarray, y_train: np.ndarray):
        self.__x_train = x_train
        self.__y_train = y_train

    def predict(self, x_test: np.ndarray) -> np.ndarray:
        y_pred = np.zeros(shape=(x_test.shape[0], 1), dtype='U20')
        num = x_test.shape[0]
        if self.__distance_metric == "cosine":
            for i in range(0, num):
                dist = self.__cos_dist(x_test[i], self.__x_train)
                dist_indices = dist.argsort()[:self.__k]
                y_pred[i] = self.__majority_voting(dist_indices, dist)
        elif self.__distance_metric == "manhattan":
            for i in range(0, num):
                dist = self.__manhat_distance(x_test[i], self.__x_train)
                dist_indices = dist.argsort()[:self.__k]
                y_pred[i] = self.__majority_voting(dist_indices, dist)
        else:
            if x_test.shape == (x_test.shape[0],):
                length = 1
            else:
                length = x_test.shape[1]
            for i in range(0, num):
                dist = self.__eucl_dist(x_test[i].reshape((1, length)), self.__x_train)
                dist_indices = dist.argsort()[:self.__k]
                # print(f"{dist} \n")
                y_pred[i] = self.__majority_voting(dist_indices, dist)
        return y_pred

    def __majority_voting(self, indices: np.ndarray, distances: np.ndarray) -> str:
        if self.__weights == "distance":
            w = 1
        else:
            w = 0
        y_train = self.__y_train
        species = np.array([0.0, 0.0, 0.0])
        for i in indices:
            if y_train[i] == "Iris-setosa":
                if distances[i] == 0:
                    species[0] += 1
                else:
                    species[0] += 1 + w*(1/distances[i] - 1)
            elif y_train[i] == "Iris-versicolor":
                if distances[i] == 0:
                    species[1] += 1
                else:
                    species[1] += 1 + w*(1/distances[i] - 1)
            else:
                if distances[i] == 0:
                    species[2] += 1
                else:
                    species[2] += 1 + w*(1/distances[i] - 1)
        if species.argmax() == 0:
            return "Iris-setosa"
        elif species.argmax() == 1:
            return "Iris-versicolor"
        return "Iris-virginica"

    def set_dist_metric(self, dist_metric: str):
        self.__distance_metric = dist_metric

    def set_weights(self, weights: str):
        self.__weights = weights

    def __eucl_dist(self, p: np.ndarray, q: np.ndarray) -> np.ndarray:
        return np.sqrt(np.sum((p-q) ** 2, -1))

    def __cos_dist(self, p: np.ndarray, q: np.ndarray) -> np.ndarray:
        cs = np.sum(p*q, -1) / np.sqrt(np.sum(p**2, -1) * np.sum(q**2, -1))
        return np.array([1]) - abs(cs)

    def __manhat_distance(self, p: np.ndarray, q: np.ndarray) -> np.ndarray:
        return np.sum(np.abs(p - q), -1)
