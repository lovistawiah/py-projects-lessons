from re import X


class PartyAnimal:
    x = 0

    def __init__(self, x):
        self.x = x

    def party(self, x):
        re = self.x = x + 1
        return re


p = PartyAnimal()
print(p.party(3))
