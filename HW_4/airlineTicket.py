from HW_4.ticket import Ticket


class AirlineTicket(Ticket):
    def __init__(self, source, destination, departure_date, price, flight_number):
        super().__init__(source, destination, departure_date, price)
        self.flight_number = flight_number

    def display_ticket_info(self):
        print(f"Flight {self.flight_number}: {self.source} to {self.destination} on \
               {self.departure_date}, Price: ${self.price}")
