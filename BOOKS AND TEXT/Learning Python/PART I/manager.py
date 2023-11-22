from person import Person
class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0+percent + bonus)


if __name__ == '__main__':
    tom = Manager('Tom Cruise', 41, 4900, 'manager of DoP')
    print(tom.lastName())
    tom.raise_pay(2)
    print(tom.pay)
