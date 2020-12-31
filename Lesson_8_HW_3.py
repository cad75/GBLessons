class OwnInputControl(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def is_valid(num):
        if num.isdigit():
            return True
        else:
            raise OwnInputControl("Ожидается число")


def pz3():
    stop_word = "stop"
    res_list = []
    while True:
        num = input("Введите число: ")
        if num == stop_word:
            break
        try:
            OwnInputControl.is_valid(num)
            res_list.append(int(num))
        except OwnInputControl as err:
            print(err)
    print("Вы ввели:", res_list)
