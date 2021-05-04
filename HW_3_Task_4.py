"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 10
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 1.5) for _ in range(SIZE)]
print(array)

num = array[0]
quantity = 1
for i in range(len(array)):
    spam = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            spam += 1
    if spam > quantity:
        quantity = spam
        num = array[i]

print(f'Число {num} встречется в массиве {quantity} раз' if quantity > 1 else 'Все элементы встречаются один раз')
