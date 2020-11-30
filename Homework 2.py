user_list = list(input("Введите значения списка без пробелов: "))
j = 0
for i in range(int(len(user_list) / 2)):
    user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
    j += 2
print(user_list)