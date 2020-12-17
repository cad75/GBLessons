import time


class TrafficLight:
    def __init__(self):
        self.__color = "red"
        self.__timings = {"red": [7, '\033[91m', "Красный"], "yellow": [2, '\033[93m', "Желтый"],
                          "green": [4, '\033[92m', "Зеленый"]}

    def __str__(self):
        return self.__color

    def __next(self):
        if self.__color == "red":
            self.__color = "yellow"
        elif self.__color == "yellow":
            self.__color = "green"
        elif self.__color == "green":
            self.__color = "red"

    def running(self, steps=3):
        if steps < 0:
            raise ValueError("Количество ходов должно быть больше нуля")
        print(f"Начали {steps} циклов")
        for i in range(steps * 3):
            color = self.__timings[self.__color]
            print(f'{color[1]}{color[2]}: {color[0]}сек. \033[0m', end="")
            for j in range(color[0]):
                print('.', end="")
                time.sleep(1)
            print(end="\n")
            self.__next()
        else:
            print("Закончили")


t = TrafficLight()
t.running()