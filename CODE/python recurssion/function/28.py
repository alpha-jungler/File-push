class Vehicle:
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model  
        self.year=year

    def display_info(self):
        print(f"Vehicle:{self.brand}, Vehicle:{self.model}, Vehicle:{self.year}")

class car(Vehicle):
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_info(self):
          print(f"Vehicle:{self.brand}, Vehicle:{self.model}, Vehicle:{self.year}")
#displaying info
X=Vehicle("Lamborghini", "Urus Se", 2025)
X.display_info()
Y=car('BMW' , "i8", 2004)
Y.display_info()

class Vehicle:
    def start(self):
        print("Vehicle  started")

class car(Vehicle):
    def drive(self):
        print ("car is driving")

c=car()
c.start()
c.drive()

    

