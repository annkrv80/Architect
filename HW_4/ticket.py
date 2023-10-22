from abc import ABC, abstractmethod


# Абстрактный класс для билетов
class Ticket(ABC):
    def __init__(self, source, destination, departure_date, price):
        self.source = source
        self.destination = destination
        self.departure_date = departure_date
        self.price = price

    @abstractmethod
    def display_ticket_info(self):
        pass
