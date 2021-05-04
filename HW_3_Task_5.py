"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""
import random

SIZE = 10
MIN_ITEM = -200
MAX_ITEM = -100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
ind_array = -1
while i < len(array):  # или for i in range(len(array)):
    if array[i] < 0 and ind_array == -1:
        ind_array = i
    elif 0 > array[i] > array[ind_array]:
        ind_array = i
    i += 1

if ind_array != -1:
    print(f'Максимальный отрицательный элемент {array[ind_array]} 'f'находится в позиции {ind_array}')
