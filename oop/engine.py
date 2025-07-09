#Define a class named Car with attributes Brand, Model, Year
class Car:
    def __init__(self,Brand, Model, Year):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year

    # Define a method to start the engine
    def start_engine(self):
        print("The engine is starting...")

    # Define a method to display the car's details
    def display_info(self):
        print(f"Brand: {self.Brand}, Model: {self.Model}, Year: {self.Year}")

#instantiate objects from the car class and call it's methods
car_1 = Car("G-wagon", "G63", "2020")

car_1.start_engine()
car_1.display_info()
