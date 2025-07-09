passenger_Name = input("Enter passenger name: ")
Weight = int(input(f"Enter weight in kg: "))

class AirlineTicket:
    def __init__(self, passenger_Name, weight):
        self.passenger_name = passenger_Name
        self.weight = weight

    def book_ticket(self):
        if self.weight <= 350:
            print(f"Dear, {self.passenger_name} you can board the flight")

        else:
            print(f"Dear, {self.passenger_name} you cannot board the flight due to excess weight.")

# Instantiate the AirlineTicket class and book a ticket
ticket = AirlineTicket(passenger_Name, Weight)

ticket.book_ticket()
