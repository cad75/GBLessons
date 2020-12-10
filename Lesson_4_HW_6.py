from itertools import count, cycle

"""
First script
"""

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

"""
Second script
"""

user_list = [3, 'a', False, 7]
c = 0
for el_2 in cycle(user_list):
    print(el_2)
    if c >= 10:
        break
    c += 1
