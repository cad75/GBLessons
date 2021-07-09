"""
Задача № 1. Отсортировать по убыванию методом «пузырька» одномерный
целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Вывести на экран исходный и отсортированный массивы.
"""

import random


def bublle_sort(array):
    n = 1

    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        stop = 0
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                stop += 1
        if stop == len(array) - 1:
            return array
    return array


array = [random.randint(-100, 99) for i in range(10)]

print('Сгенерированный массив: \n{}'.format(array))
print('Отсортированный массив:\n{}'.format(bublle_sort(array)))
