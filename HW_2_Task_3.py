"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""
KONSTAN = 10

user_num = int(input('Введите целое число: '))
revers = 0
while user_num > 0:
    revers = revers * KONSTAN + user_num % KONSTAN
    user_num = user_num // KONSTAN
print(revers)
