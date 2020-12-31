class OwnZeroDev(Exception):
    def __init__(self, txt):
        self.txt = txt


def pz2():
    inpt = input("Введите делитель: ")
    try:
        inpt = int(inpt)
        if inpt == 0:
            raise OwnZeroDev("На ноль не делим")
    except ValueError:
        print("Ожидается число")
    except OwnZeroDev as err:
        print(err)
    else:
        print(f"Результат 10/{inpt}: {10 / inpt}")
