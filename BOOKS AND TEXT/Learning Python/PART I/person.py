class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def raise_pay(self, percent):
        self.pay *= (1.0 + percent)


if __name__ == '__main__':
    bob = Person('Bob Smith', 43, 4000, 'software')
    sue = Person('Sue Jones', 40, 4000, 'hardware')

    last_name = bob.lastName()
    print(last_name)

    bob.raise_pay(23)
    print(bob.pay)
