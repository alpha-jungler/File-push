class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
t2=Person("Rikesh", 16)
print(t2.name)
print(t2.age)
print()



class car:
    def __init__(self, brand, model, year ):
        self.brand=brand
        self.model=model
        self.year=year
    def display_info(self):
        print(f"Brand Name:{self.brand}")
        print(f"Model Name:{self.model}")
        print(f"year:{self.year}")
n2=car("Lamborghini urus", "Urus Se", 2025)
g3=car("BMW", "i8", 2004)
n2.display_info()
print()
g3.display_info()


"""m6=car("Lamborghini urus", "Urus Se", 2025)
print(m6.brand)
print(m6.model)
print(m6.year)"""