with open("text_2.txt") as file:
    line = file.readlines()
    el_sum = 0
    for i in line:
        number_words = i.split()
        el_sum += int(number_words[1])
        if int(number_words[1]) < 20000:
            print(number_words)
print(el_sum / len(line))
