"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается
с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

result_array = []
for i, item in enumerate(array):
    if item % 2 == 0:
        result_array.append(i)
print(f'Индексы четных элементов: {result_array}')

new_array = [i for i in range(len(result_array)) if result_array[i] % 2 == 0]
print(f'Индексы четных элементов: {new_array}')
