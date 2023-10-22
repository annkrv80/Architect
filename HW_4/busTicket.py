from HW_4.ticket import Ticket


class BusTicket(Ticket):
    def __init__(self, source, destination, departure_date, price, trip_number):
        super().__init__(source, destination, departure_date, price)
        self.trip_number = trip_number

    def display_ticket_info(self):
        print(f"Trip {self.trip_number}: {self.source} to {self.destination} on \
               {self.departure_date}, Price: ${self.price}")