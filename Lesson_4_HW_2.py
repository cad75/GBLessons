first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = (el for i, el in enumerate(first_list[1:], 1) if el > first_list[i - 1])
print(list(result_list))
