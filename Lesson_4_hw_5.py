from functools import reduce

user_list = (el for el in range(100, 1001) if el % 2 == 0)


def composition_func(param_1, param_2):
    return param_1 * param_2


print(reduce(composition_func, user_list))
