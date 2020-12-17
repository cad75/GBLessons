class Road:
    _length = None
    _width = None

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calc_mass_of_asphalt(self, mass_per_m2, thickness):
        return self._width * self._length * mass_per_m2 * thickness


r = Road(5000, 20)

print(r.calc_mass_of_asphalt(25, 5) / 1000, 'т.')