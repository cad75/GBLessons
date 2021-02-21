"""
Давайте решать интересные задачи!
"""
def is_cyrilic(data_string, index):
    last_char = ord(data_string[index])
    if last_char >= 1072 and last_char <= 1103:
        print(f'Founded! {last_char}')
        return True
    else:
        print("Try more")
        return False

#input_string = input("Введите строчку: ")
#flag = is_cyrilic(input_string)
#print(flag)

def my_max(list_numbers):
    max_el = 0
    max_index = 0
    for i in range(len(list_numbers)):
        if list_numbers[i] > max_el:
            max_el = list_numbers[i]
            max_index = i
    print(f'Founded index {max_index}, value {max_el}')
    return [max_el, max_index]

random_list = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
result = my_max(random_list)
print(f'result {result}')

