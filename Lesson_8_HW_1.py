class Data:
    def __init__(self, date_str):
        if Data.is_valid(date_str):
            Data.date_str = date_str
        else:
            raise ValueError("Введенная строка не может быть приведена к числу")

    @classmethod
    def to_str(cls):
        dt = [int(x) for x in cls.date_str.split("-")]
        return dt[0] + dt[1] * 30 + dt[2] * 12

    @staticmethod
    def is_valid(date_str):
        try:
            list((int(x) for x in date_str.split("-")))
            return True
        except:
            return False


def pz1():
    d = Data("01-01-2020")
    print(d.to_str())
    d1 = Data("02-01-2020s")
    print(d1.to_str())
