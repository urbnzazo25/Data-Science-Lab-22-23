import matplotlib.pyplot as plt
import csv
from math import *


def mean(x, y):
    if x == '':
        x = 0.0
    if y == '':
        y = 0.0
    x = float(x)
    y = float(y)
    return (x + y) / 2


def file_open(name: str, glt: list):
    n = c = 0
    with open(name) as f:
        for cols in csv.reader(f):
            if cols:
                glt.append(cols)
                if n == 0:
                    c = len(cols)
                n += 1
    return n, c


def prev_city_line(glt: list, cities_last_indexes: dict, k: int, c: int):
    city_line = []
    for i in range(0, cols):
        city_line.append("")
    cityName = glt[k][3]
    if cityName in cities_last_indexes:
        index = cities_last_indexes.get(cityName)
        city_line = glt[index]
    cities_last_indexes[cityName] = k
    return city_line


def suc_city_line(glt: list, k: int, n: int, c: int):
    city_line = []
    for i in range(0, cols):
        city_line.append("")
    for i in range(k + 1, n):
        if glt[k][3] == glt[i][3] and glt[i][1] != '':
            city_line = glt[i]
            break
    return city_line


def temp_mean(glt: list, city: str):
    temp_means = []
    for line in glt:
        if line[3] == city:
            temp_means.append(float(line[1]))
    return temp_means


def sdm(glt: list, city: str, mean: float):
    sse = n = 0
    for line in glt:
        if line[3] == city:
            n += 1
            sse += (float(line[1]) - mean) ** 2
    return sqrt(sse / n)


def from_Fahr_to_Cels(glt: list, city: str):
    for line in glt:
        if line[3] == city:
            line[1] = (float(line[1])-32) / 1.8


if __name__ == '__main__':
    glt = []
    num, cols = file_open("glt", glt)

    cities_last_indexes = {}
    for i in range(1, num):
        if glt[i][1] == '':
            if i == 0:
                suc_line = suc_city_line(glt, i, num, cols)
                glt[i][1] = str(mean(0, suc_line[1]))
            elif i == num - 1:
                prev_line = prev_city_line(glt, cities_last_indexes, i, cols)
                glt[i][1] = str(mean(prev_line[1], 0))
            else:
                suc_line = suc_city_line(glt, i, num, cols)
                prev_line = prev_city_line(glt, cities_last_indexes, i, cols)
                glt[i][1] = str(mean(prev_line[1], suc_line[1]))
        cities_last_indexes[glt[i][3]] = i

    city = input("Write a city: ")
    n = int(input("Write an integer: "))
    city_temp = {city: []}
    for line in glt:
        if line[3] == city:
            city_temp[city].append(float(line[1]))
    city_temp[city].sort()
    highest_temps = city_temp[city][:-n - 1:-1]
    coldest_temps = city_temp[city][0:n]
    print(f"Top {n} highest temperatures: {highest_temps}")
    print(f"Top {n} coldest temperatures: {coldest_temps}")

    cities = ["Rome", "Bangkok"]
    temp_means = [temp_mean(glt, cities[0]), temp_mean(glt, cities[1])]
    plt.hist(temp_means[0], bins=100, alpha=0.5, label='Rome')
    plt.hist(temp_means[1], bins=100, alpha=0.5, label='Bangkok')
    plt.title('Distribution of temperature in Rome and Bangkok')
    plt.legend(loc='upper right')
    plt.show()

    from_Fahr_to_Cels(glt, "Bangkok")
    temp_means[1] = temp_mean(glt, cities[1])
    plt.hist(temp_means[0], bins=100, alpha=0.5, label='Rome')
    plt.hist(temp_means[1], bins=100, alpha=0.5, label='Bangkok')
    plt.title('Distribution of temperature in Rome and Bangkok')
    plt.legend(loc='upper right')
    plt.show()
