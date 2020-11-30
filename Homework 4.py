user_string = input('Введите слова: ')
for ind, el in enumerate(user_string.split(), 1):
    print(f'{ind}: {el[:10]}')