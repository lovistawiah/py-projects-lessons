class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
if __name__ =='__main__':
    bob = Person('Bob Smith',43,4000,'software')
    sue = Person('Sue Jones',40,4000,'hardware')
    jones = Person('Lovis Jones',21,4000,'Tech Lead')

    print(bob.name, sue.pay)
    print(bob.name.split()[-1])