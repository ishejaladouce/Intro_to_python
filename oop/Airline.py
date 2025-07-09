passenger_Name = input("Enter passenger name: ")
Weight = int(input(f"Enter weight in kg: "))

class AirlineTicket:
    def __init__(self, passenger_Name, weight):
        self.passenger_name = passenger_Name
        self.weight = weight

#Add inheritance to the AirlineTicket class
# The Booking class will inherit from the AirlineTicket class
Flight_number = input("Enter flight number: ")
class Booking (AirlineTicket):
    def __init__(self,passenger_Name, weight, Flight_number):
        self.Flight_number = Flight_number
        super().__init__(passenger_Name, weight)

# Define a method to book a ticket that checks the weight limit
    def book_ticket(self):
        if self.weight <= 350:
            print(f"Dear, {self.passenger_name}, with flight number {self.Flight_number} you can board the flight")

        else:
            print(f"Dear, {self.passenger_name}, with flight number {self.Flight_number} you cannot board the flight due to excess weight.")

# Instantiate the AirlineTicket class and book a ticket
ticket = Booking(passenger_Name, Weight, Flight_number)

ticket.book_ticket()
