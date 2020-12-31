class BaseEquip:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Printer(BaseEquip):
    def __init__(self, paper, name):
        super().__init__(name)
        self.paper = paper


class Scaner(BaseEquip):
    def __init__(self, speed, name):
        super().__init__(name)
        self.speed = speed


class Xerox(BaseEquip):
    def __init__(self, is_color, name):
        super().__init__(name)
        self.is_color = is_color


class EquipsCountControl(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def is_valid(count):
        if isinstance(count, str):
            raise EquipsCountControl("Количество должно быть числом")
        elif count < 0:
            raise EquipsCountControl("Количество должно быть числом больше нуля")
        else:
            return True


class Warehouse:
    def __init__(self):
        self._last_index = 0
        self._equips = []
        self._section = [{"name": "Отдел ремонта", 'equips': []},
                         {"name": "Отдел продаж", 'equips': []},
                         {"name": "Отдел закупок", 'equips': []}]

    @property
    def equips(self):
        return [self.__equip_str(x) for x in self._equips]

    def __equip_str(self, equip):
        k = list(equip.keys())[0]
        v = equip[k]
        return {k: str(v)}

    @property
    def sections(self):
        res = []
        for s in self._section:
            ss = s
            ss['equips'] = [str(list(x.values())[0]) for x in s['equips']]
            res.append(ss)
        return res

    def add_equips(self, equip, count):
        try:
            EquipsCountControl.is_valid(count)
            for i in range(count):
                self.add_equip(equip)
        except EquipsCountControl as err:
            print(err)

    def add_equip(self, equip: BaseEquip):
        self._equips.append({self._last_index: equip})
        self._last_index += 1

    def send_equip_to_section(self, equip_index, section_index):
        self._section[section_index]['equips'].append(self._equips[equip_index])


x = Xerox(True, "My favorite xerox")

w = Warehouse()
w.add_equip(x)
w.send_equip_to_section(0, 1)

print(w.equips)
print(w.sections)

p = Printer(500, "My printer")
cnt = 0
while True:
    try:
        cnt = int(input("Введите число принтеров: "))
        EquipsCountControl.is_valid(cnt)
        break
    except EquipsCountControl as err:
        print(err)
    except:
        print("Ожидается число")

w.add_equips(p, cnt)

print(w.equips)