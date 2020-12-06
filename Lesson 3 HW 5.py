def summ_numbers():
    res = 0
    is_enough = False
    while not is_enough:
        in_list = input('Введите числа через пробел: ').split()
        for el in in_list:
            try:
                res += float(el)
            except:
                is_enough = True
        print(res)
"""
Второй вариант
if el != "e":
    res += float(el)
else:
    is_enough = True
"""
print(summ_numbers())
