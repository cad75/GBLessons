"""
Задача № 1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС.
"""

""" 
Версия Python: python 3.9
ОС: macOS High Sierra 10.13.6 
"""

import sys


def show_size(x, level=0):
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par


# Урок 1 задача № 1.

a = input('Введите трехзначное число: ')

x = int(a[0])
y = int(a[1])
z = int(a[2])

sum_l = x + y + z
mult = x * y * z

sum_member = sys.getsizeof(a) + sys.getsizeof(x) + sys.getsizeof(y) + sys.getsizeof(z) + sys.getsizeof(
    sum_l) + sys.getsizeof(mult)
print('В программе задействовано байт памяти: {}'.format(sum_member))

# Результат запуска программы и измерения:
#
# Введите трехзначное число: 999
#
# В программе задействовано байт памяти: 192

# ===============================================

# Урок 2, задача № 3.

new_num = ''
num = input('Введите число: ')
count = len(num)
k = range(count)

for i in k:
    new_num = new_num + str(int(num) % 10)
    num = int(num) // 10
print(new_num)

sum_member2 = show_size(new_num) + show_size(num) + show_size(count) + show_size(k)
print('В программе задействовано байт памяти: {}'.format(sum_member2))

# Результат запуска программы и измерения:
#
# Введите число: 4567
# 7654
# type=<class 'str'>, size=53, object=7654
#  type=<class 'int'>, size=24, object=0
#  type=<class 'int'>, size=28, object=4
#  type=<class 'range'>, size=48, object=range(0, 4)
# 	 type=<class 'int'>, size=24, object=0
# 	 type=<class 'int'>, size=28, object=1
# 	 type=<class 'int'>, size=28, object=2
# 	 type=<class 'int'>, size=28, object=3
# В программе задействовано байт памяти: 261

# ===============================================

# Урок 2, задача № 2.

import random

g = range(9)

mas_num = [random.randint(1, 100) for n in g]
print('Дан массив элементов: {}'.format(mas_num))

mas_index = [mas_num.index(i) for i in mas_num if i % 2 == 0]
print('Массив индексов четных элементов: {}'.format(mas_index))

sum_member3 = show_size(mas_num) + show_size(num) + show_size(g)
print('В программе задействовано байт памяти: {}'.format(sum_member3))
# Результат запуска программы и измерения:
#
# Дан массив элементов: [20, 77, 22, 87, 45, 76, 10, 3, 67]
# Массив индексов четных элементов: [0, 2, 5, 6]
#  type=<class 'list'>, size=184, object=[20, 77, 22, 87, 45, 76, 10, 3, 67]
# 	 type=<class 'int'>, size=28, object=20
# 	 type=<class 'int'>, size=28, object=77
# 	 type=<class 'int'>, size=28, object=22
# 	 type=<class 'int'>, size=28, object=87
# 	 type=<class 'int'>, size=28, object=45
# 	 type=<class 'int'>, size=28, object=76
# 	 type=<class 'int'>, size=28, object=10
# 	 type=<class 'int'>, size=28, object=3
# 	 type=<class 'int'>, size=28, object=67
#  type=<class 'int'>, size=24, object=0
#  type=<class 'range'>, size=48, object=range(0, 9)
# 	 type=<class 'int'>, size=24, object=0
# 	 type=<class 'int'>, size=28, object=1
# 	 type=<class 'int'>, size=28, object=2
# 	 type=<class 'int'>, size=28, object=3
# 	 type=<class 'int'>, size=28, object=4
# 	 type=<class 'int'>, size=28, object=5
# 	 type=<class 'int'>, size=28, object=6
# 	 type=<class 'int'>, size=28, object=7
# 	 type=<class 'int'>, size=28, object=8
# В программе задействовано байт памяти: 756
