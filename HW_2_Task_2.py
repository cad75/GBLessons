"""
Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def even_odd(number, even_=0, odd_=0):
    if number == 0:
        return even_, odd_
    if number % 2 == 0:
        even_ += 1
    else:
        odd_ += 1
    number = number // 10
    return even_odd(number, even_, odd_)


num = int(input('Введите натуральное число: '))
print(even_odd(num))
