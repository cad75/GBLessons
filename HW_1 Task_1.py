# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
user_num = int(input('целое число: '))
f_num = user_num // 100
middle_num = user_num // 10
s_num = middle_num % 10
th_num = user_num % 10
print(f_num + s_num + th_num)
print(f_num + s_num + th_num)
