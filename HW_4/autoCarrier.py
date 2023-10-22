from HW_4.busTicket import BusTicket
from HW_4.carrier import Carrier


class AutoCarrier(Carrier):
    def sell_ticket(self, user, source, destination, departure_date):
        # Логика продажи авиабилета
        ticket = BusTicket(source, destination, departure_date, 20, "123")
        return ticket