from HW_4.airline import AirlineCarrier
from HW_4.autoCarrier import AutoCarrier
from HW_4.bankAccount import BankAccount
from HW_4.user import User


user1 = User("Alice", "alice@email.com")
bank_account = BankAccount("Alice", 1000)

airline_carrier = AirlineCarrier("Sample Airlines")
auto_carrier = AutoCarrier("Red buses")

# Продажа авиабилета
airline_ticket = airline_carrier.sell_ticket(user1, "City A", "City B", "2023-10-31")
if bank_account.withdraw(airline_ticket.price):
    print("Airline ticket purchased:")
    airline_ticket.display_ticket_info()
else:
    print("Insufficient funds for airline ticket purchase.")

# Продажа билета на автобус
bus_ticket = auto_carrier.sell_ticket(user1, "City A", "City B", "2023-10-31")
if bank_account.withdraw(bus_ticket.price):
    print("Bus ticket purchased:")
    bus_ticket.display_ticket_info()
else:
    print("Insufficient funds for bus ticket purchase.")
