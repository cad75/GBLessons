def my_func(numb_1, numb_2, numb_3):
    all_number = {numb_1, numb_2, numb_3}
    result = max(all_number)
    all_number.remove(result)
    result += max(all_number)
    return result
"""
А можно тело функции сделать так!
    #if numb_1 and numb_2 >= numb_3:
       # return numb_1 + numb_2
   # elif numb_2 and numb_3 >= numb_1:
      #  return numb_2 + numb_3
   # else:
        #return numb_1 + numb_3
"""
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
print(f' Сумма максимальных чисел равна: {my_func(number_1, number_2, number_3)}')

