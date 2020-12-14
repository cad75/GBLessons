with open("text_1.txt") as file:
    line = file.readlines()
    print('В файле:', len(line), ' строк(строки)')
    for i, value in enumerate(line):
        number_words = len(value.split())
        print('В строке {} находится {} слов.\n'.format(i + 1, number_words))
