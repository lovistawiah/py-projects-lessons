class Vehicle:
    def __init__(self, doors, wheels, engine_type, color, seat, name):
        self.doors = doors
        self.wheels = wheels
        self.engine_type = engine_type
        self.color = color
        self.seat = seat
        self.name = name

    def parts(self):
        return f'{self.name} has {self.engine_type}, {self.doors} doors, {self.wheels} wheels ,{self.color} color and {self.seat} seats'


class Honda(Vehicle):
    def __init__(self, doors, wheels, engine_type, color, seat, name, location, head_quaters):
        self.location = location
        self.head_quaters = head_quaters

        Vehicle.__init__(self, doors, wheels, engine_type, color, seat, name)

    def company(self):
        return f"{self.name}'s {self.head_quaters} is located at {self.location}"


Honda = Honda('4', '4', 'v6 engine', 'green', '5',
              'Honda Civic', 'Berlin', 'Honda, Inc')

print(Honda.parts())
print(Honda.company())


my_tuple = ('abc', 123, 'def', 456)
print(my_tuple)
groceries = {'fruits': ['mangoes', 'bananas', 'kiwis'],
             'protein': ['beef', 'pork', 'salmon'],
             'carbs': ['rice', 'pasta', 'bread'],
             'veggies': ['lettuce', 'cabbage', 'onions']}

for key, items in groceries.items():
    for item in items:
        print('{} found in  {}'.format(item, key))

students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}

students3 = students1.union(students2)
print(students3)
