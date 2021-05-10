"""
Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import cProfile
from timeit import timeit

user_num = int(input('целое число: '))


def num_simple():
    f_num = user_num // 100
    middle_num = user_num // 10
    s_num = middle_num % 10
    th_num = user_num % 10
    summ_ = f_num + s_num + th_num
    digit_ = f_num * s_num * th_num
    return summ_, digit_


# print(num_simple())


print(timeit('num_simple()', number=10000, globals=globals()))
cProfile.run('num_simple()')

'''
Результат данной реализации кода является самым быстрым.
'''

# целое число: 234
# 0.005185668999999837
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW_4_Task_1.py:13(num_simple)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


user_num_2 = int(input('целое число: '))
user_num_2 = str(user_num_2)


def num_simple_2():
    user_sum = 0
    user_increase = 1
    for i in user_num_2:
        user_sum += int(i)
        user_increase *= int(i)
    return user_sum, user_increase


# print(num_simple_2())

print(timeit('num_simple_2()', number=10000, globals=globals()))
cProfile.run('num_simple_2()')

'''
Самый затратный способ реализации задачи.
'''

# целое число: 234
# 0.01654252300000003
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW_4_Task_1.py:33(num_simple_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

user_num_3 = int(input('целое число: '))
user_num_3 = str(user_num_3)


def num_simple_3():
    f_num = int(user_num_3[0])
    s_num = int(user_num_3[1])
    th_num = int(user_num_3[2])
    summ_ = f_num + s_num + th_num
    mult_ = f_num * s_num * th_num
    return summ_, mult_


# print(num_simple_3())

print(timeit('num_simple_3()', number=10000, globals=globals()))
cProfile.run('num_simple_3()')

'''
Средняя по затратам реализация.
'''

# целое число: 234
# 0.010266192999999646
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW_4_Task_1.py:51(num_simple_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
