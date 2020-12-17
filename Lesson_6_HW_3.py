class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 12, "bonus": 3}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p1 = Position()
p1.name = "Vasya"
p1.surname = "Petin"
print(p1.get_full_name())
print(p1.get_total_income())