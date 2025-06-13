class Student:
    def __init__(self, name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display_details(self):
        print(f"Name:{self.name}, Age:{self.age}, Grade:{self.grade}")

#creating students as objects

Student1=Student("Rikesh", 16, 5)
Student2=Student("Lizen", 16, 5)
Student3=Student("Ranjit", 17, 6)
Student4=Student("Newson", 18, 8)
Student5=Student("Zaid", 17, 8)

#displaying students details
print()
Student1.display_details()
print()
Student2.display_details()
print()
Student3.display_details()
print()
Student4.display_details()
print()
Student5.display_details()