import csv
import copy

if __name__ == '__main__':
    iris = []
    with open("iris.data") as f:
        for cols in csv.reader(f):
            if cols:
                iris.append(cols)
    n = len(iris)

    mean = {'sLength': 0.0, 'sWidth': 0.0, 'pLength': 0.0, 'pWidth': 0.0}
    stdDev = {'sLength': 0.0, 'sWidth': 0.0, 'pLength': 0.0, 'pWidth': 0.0}

    num = [0, 0, 0]
    vers = [copy.deepcopy(mean), copy.deepcopy(stdDev), num[0]]
    virg = [copy.deepcopy(mean), copy.deepcopy(stdDev), num[1]]
    set = [copy.deepcopy(mean), copy.deepcopy(stdDev), num[2]]

    for i in range(0, n):
        j = 0
        for k in mean.keys():
            mean[k] += float(iris[i][j])
            j += 1
    for k in mean.keys():
        mean[k] = mean[k]/n
    print(f"Total mean: {mean.values().mapping}")

    for i in range(0, n):
        j = 0
        for k in stdDev.keys():
            stdDev[k] += (float(iris[i][j]) - mean[k]) ** 2
            j += 1
    for k in stdDev.keys():
        stdDev[k] = (stdDev[k]/n) ** 0.5
    print(f"Total standard deviation: {stdDev.values().mapping}")

    for i in range(0, n):
        if iris[i][4]=='Iris-versicolor':
            vers[2] += 1
            j = 0
            for k in dict(vers[0]).keys():
                vers[0][k] += float(iris[i][j])
                j += 1
        elif iris[i][4]=='Iris-virginica':
            virg[2] += 1
            j = 0
            for k in dict(virg[0]).keys():
                virg[0][k] += float(iris[i][j])
                j += 1
        else:
            set[2] += 1
            j = 0
            for k in dict(set[0]).keys():
                set[0][k] += float(iris[i][j])
                j += 1
    for k in dict(vers[0]).keys():
        vers[0][k] /= vers[2];
    print(f"Iris Versicolor mean: {dict(vers[0]).values().mapping}")
    for k in dict(virg[0]).keys():
        virg[0][k] /= virg[2];
    print(f"Iris Virginica mean: {dict(virg[0]).values().mapping}")
    for k in dict(set[0]).keys():
        set[0][k] /= set[2];
    print(f"Iris Setosa mean: {dict(set[0]).values().mapping}")

    for i in range(0, n):
        if iris[i][4]=='Iris-versicolor':
            j = 0
            for k in dict(vers[1]).keys():
                vers[1][k] += (float(iris[i][j]) - vers[0][k]) ** 2
                j += 1
        elif iris[i][4]=='Iris-virginica':
            j = 0
            for k in dict(virg[1]).keys():
                virg[1][k] += (float(iris[i][j]) - virg[0][k]) ** 2
                j += 1
        else:
            j = 0
            for k in dict(set[1]).keys():
                set[1][k] += (float(iris[i][j]) - set[0][k]) ** 2
                j += 1
    for k in dict(vers[1]).keys():
        vers[1][k] = (vers[1][k] / vers[2]) ** 0.5
    print(f"Iris Versicolor sdv: {dict(vers[1]).values().mapping}")
    for k in dict(virg[1]).keys():
        virg[1][k] = (virg[1][k] / virg[2]) ** 0.5
    print(f"Iris Virginica sdv: {dict(virg[1]).values().mapping}")
    for k in dict(set[1]).keys():
        set[1][k] = (set[1][k] / set[2]) ** 0.5;
    print(f"Iris Setosa sdv: {dict(set[1]).values().mapping}")