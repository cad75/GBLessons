class Cell:
    def __init__(self, nucleus: int):
        if nucleus < 0:
            raise ValueError("Количество клеток ячейки должно быть больше нуля")
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if self.nucleus - other.nucleus > 0:
            return Cell(self.nucleus - other.nucleus)
        else:
            raise ValueError("Невозможно вычислить разность клеток, если она меньше нуля")

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(self.nucleus // other.nucleus)

    def __str__(self):
        return str(self.nucleus)

    def make_order(self, row_size):
        res = ""
        for i in range(1, self.nucleus + 1):
            res += "*"
            if i % row_size == 0:
                res += "\n"
        return res


c1 = Cell(10)
c2 = Cell(5)
c3 = Cell(15)

print(f"Сложение 10 и 5: {c1 + c2}")
print(f"Вычитание 10 и 5: {c1 - c2}")
print(f"Умножение 10 и 5: {c1 * c2}")
print(f"Деление 15 на 5: {c3 / c2}")
print("10 по 3 в строке:")
print(c1.make_order(3))
print("5 по 3 в строке:")
print(c2.make_order(3))
print("15 по 4 в строке:")
print(c3.make_order(4))
