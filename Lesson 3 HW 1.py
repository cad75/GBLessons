def division_func(num_1, num_2):
        return num_1 / num_2
try:
    number_1 = float(input('Введите целое число: '))
    number_2 = float(input('Введите второе число: '))
    print(division_func(number_1, number_2))
except ZeroDivisionError:
    print('На ноль делить нельзя')

"""
А можно так! Тогда при делении на ноль пользователю снова предложат совержить ввод чисел.
while number_2 == 0:
print('На ноль делить нельзя')
number_1 = float(input('Введите целое число: '))
number_2 = float(input('Введите второе число: '))
print(division_func(number_1, number_2))
"""




