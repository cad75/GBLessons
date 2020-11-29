month_number = int(input('Введите номер месяца года: '))
year_list = ['Зима', 'Весна', 'Лето', 'Осень']
if month_number == 1 or month_number == 2 or month_number == 12:
    print(year_list[0])
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(year_list[1])
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(year_list[2])
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(year_list[3])

user_number = int(input('Введите номер месяца года: '))
year_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if user_number == 1 or user_number == 2 or user_number == 12:
    print(year_dict.get(1))
elif user_number == 3 or user_number == 4 or user_number == 5:
    print(year_dict.get(2))
elif user_number == 6 or user_number == 7 or user_number == 8:
    print(year_dict.get(3))
elif user_number in [9, 10, 11]:
    print(year_dict.get(4))