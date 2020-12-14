with open("text.txt", 'w') as f:
    while True:
        user_string = input('Внесите данные в файл: ')
        f.write(user_string + '\n')
        if user_string == '':
            break
