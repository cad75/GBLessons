"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

FIRST_NUM = 2
END_NUM = 99
START_NUM = 2
FINISH_NUM = 9

for i in range(START_NUM, FINISH_NUM + 1):
    quantity = 0
    for j in range(FIRST_NUM, END_NUM + 1):
        if j % i == 0:
            quantity += 1
    print(f'В диапазоне от 2 до 99 числу {i} кратно {quantity} чисел')
