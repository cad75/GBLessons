user_word = input('Введите слова с маленькой буквы разделенные пробелом: ')
def my_func_list():
    user_lisl = []
    for el in user_word.split():
        user_lisl.append(el.capitalize())
    return user_lisl
print(my_func_list())
