number=int(input("Enter a number"))
if number %2 ==0:
    print(f"The number{number}is even")
else:
    print(f"The number{number}is odd")
print("Invalid number entered")

class Student:
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
    def display(self):
            print(f"Name:{self.name}")
            print(f"Grade:{self.grade}")
x=Student("Rikesh", 6)
x.display() 

"""7)	Create a base class Animal with a method make_sound() that prints "Animal sound".
Create two subclasses:
•	Dog that overrides make_sound() to print "Dog barks"
•	Cat that overrides make_sound() to print "Cat meows"
Create one object of each and call the make_sound() method for each."""

"""class Animal:
    def make_sound():
        print("Animal sound")

class Dog(Animal):"""
    
        