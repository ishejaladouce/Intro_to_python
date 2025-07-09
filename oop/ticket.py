#develop a functional airline ticketing system that manages passenger booking while adhering to a weight limit of 350
#book a passenger ticket with a aspecified weight
class Ticket:
    def __init__(self, passenger_name, weight):
        self.passenger_name = passenger_name
        self.weight = weight

    def book_ticket(self):
        if self.weight > 350:
            return "Booking failed: Weight exceeds the limit of 350kg."
        else:
            return f"Ticket booked successfully for {self.passenger_name} with weight {self.weight}kg."
        
#instantiate the Ticket class and book a ticket
ticket_1 = Ticket("John Doe", 300)
ticket_2 = Ticket("Jane Smith", 400)

ticket_1.book_ticket()