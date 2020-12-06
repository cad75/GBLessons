def get_power(x, y):
    return x ** y

el_x = float(input('Введите действительное положительное число: '))
el_y = int(input('Введите целое отрицательное число: '))
print(get_power(el_x, el_y))

def get_power_2(x, y):
    z = 1
    for i in range(abs(y)):
        z *= x
    if y >= 0:
        return z
    else:
        return 1 / z

el_x_2 = float(input('Введите действительное положительное число: '))
el_y_2 = int(input('Введите целое отрицательное число: '))
print(get_power_2(el_x_2, el_y_2))




