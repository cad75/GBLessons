# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
num = int(input('введите номер буквы: '))
num = ord('a') + num - 1
print(chr(num))