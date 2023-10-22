from abc import ABC, abstractmethod


class Carrier(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sell_ticket(self, user, source, destination, departure_date):
        pass
