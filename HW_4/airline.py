from HW_4.airlineTicket import AirlineTicket
from HW_4.carrier import Carrier


class AirlineCarrier(Carrier):
    def sell_ticket(self, user, source, destination, departure_date):
        # Логика продажи авиабилета
        ticket = AirlineTicket(source, destination, departure_date, 200, "ABC123")
        return ticket
