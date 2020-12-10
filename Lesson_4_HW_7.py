from math import factorial


def fact_func(n):
    for el in range(1, n + 1):
        yield factorial(el)


for el in fact_func(5):
    print(el)
