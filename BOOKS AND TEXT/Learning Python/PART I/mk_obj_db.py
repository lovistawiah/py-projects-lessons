from person_start import Person

bob = Person('Bob Smith', 43, 4000, 'National Security')
sue = Person('Sue Jones', 23, 4000, 'African Security')

people = [bob, sue]
for person in people:
    print(person.name, person.age, person.job)
