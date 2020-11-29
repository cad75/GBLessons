my_list = [9, 5, 2, 2, 0]
for i in range(3):
    user_num = int(input('Введите свое число, чтобы добавить в список: '))
    if user_num > max(my_list):
        my_list.insert(0, user_num)
    elif user_num <= min(my_list):
        my_list.append(user_num)
    elif my_list.count(user_num) > 1:
        ind = my_list.index(user_num) + my_list.count(user_num)
        my_list.insert(ind, user_num)
    else:
        for pos in my_list:
            if user_num > pos:
                my_list.insert(my_list.index(pos), user_num)
                break
    print(my_list)