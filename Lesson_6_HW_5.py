class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером")


print('-'*20)
s = Stationery()
s.draw()

pn = Pen()
pn.draw()

pncl = Pencil()
pncl.draw()

h = Handle()
h.draw()