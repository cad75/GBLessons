# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
one_n = int(input('введите первое целое число: '))
two_n = int(input('введите второе целое число: '))
three_n = int(input('введите третье целое число: '))
if one_n <= two_n <= three_n or three_n <= two_n <= one_n:
    print(two_n)
elif two_n <= three_n <= one_n or one_n <= three_n <= two_n:
    print(three_n)
else:
    print(one_n)
