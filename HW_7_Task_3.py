"""
Задача № 3. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найти в массиве медиану. Медианой называется
элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше ее.
Задачу можно решить без сортировки исходного массива. Но если это
слишком сложно, то используйте метод сортировки, который не
рассматривался на уроках.
"""

import random


def fi_med(array):
    for i in range(len(array) - 1):

        left = 0
        right = 0
        equal = 0

        for j in range(len(array)):

            if i != j:

                if array[i] > array[j]:
                    left += 1
                elif array[i] < array[j]:
                    right += 1
                elif array[i] == array[j]:
                    equal += 1

        if left == right:
            return array[i]

        else:
            if abs(left - right) - equal == 0:
                return array[i]


SIZE = 7
array = [random.randint(- SIZE, SIZE) for i in range(2 * SIZE - 1)]

print('Сгенерированный массив: \n{}'.format(array))
print('Медианой массива является число: {}'.format(fi_med(array)))
