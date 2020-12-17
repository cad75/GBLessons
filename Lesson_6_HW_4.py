class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def go(self, speed):
        print(f'Скорость изменена: {speed}')
        self.speed = speed

    def stop(self):
        print('Остановка')
        self.speed = 0

    def turn(self, direction):
        print(f"Должна повернуть {direction}, но никто за этим не следит")

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость этого авто превышена на {self.speed - 60}")
        print(f'Текущая скорость: {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость этого авто превышена на {self.speed - 40}")
        print(f'Текущая скорость: {self.speed}')


print('-'*20)
tc = TownCar()
tc.speed = 120
tc.name = "Any town car"
tc.color = "Red"
tc.is_police = False
print('Машина: ' + tc.name + '. Цвет: ' + tc.color + f'. Полицейская? {tc.is_police}')
tc.show_speed()
tc.stop()
tc.show_speed()
tc.go(60)
tc.show_speed()
tc.turn("налево")

print('-'*20)
wc = WorkCar()
wc.speed = 120
wc.name = "It's the Work car"
wc.color = "White"
wc.is_police = False
print('Машина: ' + wc.name + '. Цвет: ' + wc.color + f'. Полицейская? {wc.is_police}')
wc.show_speed()
wc.stop()
wc.show_speed()
wc.go(60)
wc.show_speed()
wc.turn("направо")

print('-'*20)
pc = Car()
pc.speed = 180
pc.name = "It's the Police"
pc.color = "Blue"
pc.is_police = True
print('Машина: ' + pc.name + '. Цвет: ' + pc.color + f'. Полицейская? {pc.is_police}')
pc.show_speed()
pc.stop()
pc.show_speed()
pc.go(60)
pc.show_speed()
pc.turn("наверх")

print('-'*20)