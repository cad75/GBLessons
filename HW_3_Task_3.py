"""
В массиве случайных целых чисел поменять местами минимальный и максимальный
элементы.
"""

import random

N = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)]
print(array)

meaning_min = 0
meaning_max = 0
for i in range(len(array)):
    if array[i] < array[meaning_min]:
        meaning_min = i
    elif array[i] > array[meaning_max]:
        meaning_max = i

array[meaning_min], array[meaning_max] = array[meaning_max], array[meaning_min]
print(array)
