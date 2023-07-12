import csv
from math import *


def eu_dist(x, y):
    sum = 0
    for i, j in zip(x, y):
        sum += (int(i) - int(j))**2
    return sqrt(sum)


if __name__ == '__main__':
    digits = []
    num = 0
    r = 784
    c = 28
    with open("mnist") as f:
        for cols in csv.reader(f):
            if cols:
                num += 1
                digits.append(cols)

    for i in range(0, int(num/1000)):
        print(f"Digit number {i} = {digits[i][0]}:")
        for j in range(0, r):
            if j != 0 and j % c == 0:
                print("")
            elif 0 <= int(digits[i][j]) < 64:
                print(" ", end='')
            elif 64 <= int(digits[i][j]) < 128:
                print(".", end='')
            elif 128 <= int(digits[i][j]) < 192:
                print("*", end='')
            else:
                print("#", end='')
        print("")

    chosenDigits = {"26": digits[25], "30": digits[29], "32": digits[31], "35": digits[34]}
    chosenEuDist = {}
    for i, (k1, v1) in enumerate(chosenDigits.items()):
        for j, (k2, v2) in enumerate(chosenDigits.items()):
            if j > i:
                chosenEuDist[f"{k1} - {k2}"] = eu_dist(v1[1:], v2[1:])
    print(chosenEuDist.items())