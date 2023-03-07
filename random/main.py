"""Дано;
функция random.random
Необходимо:
написать реализацию random.shuffle для массива произвольных элементов
Дополнительный плюс: написать unit-test"""

import random
from typing import List


def shaff(arr: list):
    for i in range(len(arr) - 1, 0, -1):
        j = int(random.random() * i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    arr = [3, 6, 13, 2, 7, 9]
    print(shaff(arr))
