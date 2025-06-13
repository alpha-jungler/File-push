"""class Animal:
    def make_sound(self):
        print("Animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")
class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")
def abc(animal):
    animal.make_sound()

animals=[Dog(), Cat()]
for animal in animals:
    print(abc(animal))"""


class Vehicle:
    def make_sound(self):
        print("Vehicle sound")

class car(Vehicle):
    def make_sound(self):
        print("Vroom Vroom")


class boat(Vehicle):
    def make_sound(self):
        print("Flap Flap")

class plane(Vehicle):
    def make_sound(self):
        print("Hum Hum")

def mno(vehicle):
    vehicle.make_sound()

vehicles=[car(), boat(), plane()]
for vehicle in vehicles:
    print(mno(vehicle))

        

