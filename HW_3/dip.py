from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class DieselEngine(Engine):
    def start(self):
        print("Starting Diesel Engine")


class PetrolEngine(Engine):
    def start(self):
        print("Starting Petrol Engine")


class GasEngine(Engine):
    def start(self):
        print("Starting Gas Engine")


class Car():
    def __init__(self, engine: Engine):
        self.engine = engine

    def star_engine(self):
        self.engine.start()


if __name__ == '__main__':
    car_diesel = Car(DieselEngine())
    car_diesel.star_engine()
    car_petrol = Car(PetrolEngine())
    car_petrol.star_engine()
    car_gas = Car(GasEngine())
    car_gas.star_engine()
