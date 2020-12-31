class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNum(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        z = '' if self.b < 0 else "+"
        return f'({self.a}{z}{self.b}i)'


c1 = ComplexNum(5, -6)
c2 = ComplexNum(-3, 2)
print(c1 + c2)

c3 = ComplexNum(2, 3)
c4 = ComplexNum(-1, 1)
print(c3 * c4)