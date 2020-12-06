def my_profile(first_name, last_name, birthday, city, e_mail, phone_number):
    print(f"Имя - {first_name}; Фамилия - {last_name}; Дата рождения - {birthday}; Город - {city}; Электронная почта - {e_mail}; Номер телефона - {phone_number}")

my_name = input('Укажите имя: ')
my_surname = input('Укажите фамилию: ')
my_birthday = input('Укажите дату рождения: ')
my_city = input('Укажите город: ')
my_mail = input('Укажите e-mail: ')
my_phone = input('Укажите номер телефона: ')
print(my_profile(my_name, my_surname, my_birthday, my_city, my_mail, my_phone))
