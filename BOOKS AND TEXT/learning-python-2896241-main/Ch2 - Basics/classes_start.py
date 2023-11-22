#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, body_style):
        self.body_style = body_style

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

    def park(self,bool):
        if bool:
            print("My ca")

class Car(Vehicle):
    def __init__(self, engine_type):
        super().__init__("Car")
        self.engine_type = engine_type
        self.wheels = 4
        self.doors = 4

    def drive(self, speed):
        super().drive(speed)
        print("I am driving my", self.engine_type, "car at", self.speed)


class Motor_Cycle(Vehicle):
    def __init__(self, engine_type, has_side_car):
        super().__init__("Motor_Cycle")
        if has_side_car:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engine_type = engine_type

    def drive(self, speed):
        super().drive(speed)
        print("I am driving my", self.engine_type, "motorcycle at", self.speed)


car1 = Car("gas")
car2 = Car("electric")

motor1 = Motor_Cycle("gas", True)

print(motor1.engine_type)
print(car1.engine_type)
print(car2.doors)


car1.drive(50)
motor1.drive(68)
car2.drive(10)