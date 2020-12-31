from abc import ABC, abstractmethod


class AClothes(ABC):

    @abstractmethod
    def get_cloth_count(self):
        pass


class Coat(AClothes):
    def __init__(self, v):
        self.v = v

    def get_cloth_count(self):
        return self.v / 6.5 + 0.5


class Costume(AClothes):
    def __init__(self, h):
        self.h = h

    def get_cloth_count(self):
        return 2 * self.h + 0.3

    @property
    def cloth_count(self):
        return self.get_cloth_count()


coat = Coat(55)
print(f"Кол-во ткани на пальто: {coat.get_cloth_count()}")
costume = Costume(180)
print("Кол-во ткани на костюм:")
print("As property: " + str(costume.cloth_count))
print("As method: " + str(costume.get_cloth_count()))

print('*' * 20)
