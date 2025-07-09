class Car:

     def __init__(self,Model, Price, Color, BuildYear):
         self.Model=  Model
         self.Price= Price
         self.Color = Color
         self.BuildYear= BuildYear

     def describe(self):
         print(f"{self.Model} cost {self.Price}  it has {self.Color} color and was built in {self.BuildYear}")

car_1=Car("Audi","10k","Orange","2015")
car_2=Car("Nissan","$60,000","Grey","2021")
car_3=Car("Volvo","$100,000","black","2020")

car_3.describe()