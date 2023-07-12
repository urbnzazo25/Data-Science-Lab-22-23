import pandas as pd
from KNearestNeighbors import *


def x_y_init(df: pd.DataFrame, fraction: float):
    df_test = df.sample(frac=fraction)
    # print(df_test.to_string())
    df_train = df.drop(df_test.index)
    x_test = (df_test.iloc[:, :4:]).values
    # print(x_test)
    y_test = (df_test.iloc[:, -1]).values
    # print(y_test)
    x_train = (df_train.iloc[:, :4:]).values
    y_train = (df_train.iloc[:, -1]).values
    return x_test, y_test, x_train, y_train


def compute_accuracy(pred: np.ndarray, test: np.ndarray) -> float:
    correct = 0
    for i in range(0, len(pred)):
        if pred[i] == test[i]:
            correct += 1
    return correct/len(pred)


if __name__ == '__main__':
    k = 12
    iris_db = pd.read_csv("iris.data", header=None,
                          names=["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"])
    # print(iris_db.to_string())
    frac = 0.12
    X_test, Y_test, X_train, Y_train = x_y_init(iris_db, frac)
    knn = KNearestNeighbors(k)
    knn.fit(X_train, Y_train)
    # knn.set_dist_metric("cosine")
    knn.set_weights("distance")
    Y_pred = knn.predict(X_test)
    accuracy = compute_accuracy(Y_pred, Y_test)
    print(f"The accuracy of the knn model is: {accuracy*100:.2f}%")
