class Car:

    def __init__(self, Model, Price, Color, Build_Year):
        self.Model = Model
        self.Price = Price
        self.Color = Color
        self.Build_Year = Build_Year

    def description(self):
        print(f"{self.Model}, {self.Price}, {self.Color}, {self.Build_Year}")
    
Car_1 = Car("Audi", "10k", "Orange", "2015")
Car_2 = Car("Toyota", "20k", "Blue", "2018")
Car_3 = Car("G-wagon", "150k", "Black", "2020")

Car_1.description()
Car_2.description()
Car_3.description()