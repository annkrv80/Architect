from random import randint, choice
from abc import ABC, abstractmethod


class ItemFabric(ABC):
    def __init__(self):
        self.game_item = None

    @abstractmethod
    def create_item(self):
        pass

    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class GoldReward(IGameItem):
    def open(self):
        print('Gold')


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GoldReward()


class GemReward(IGameItem):
    def open(self):
        print('Gem')


class GemGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GemReward()


class AppleReward(IGameItem):
    def open(self):
        print('Apple')


class AppleGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return AppleReward()


class AxeReward(IGameItem):
    def open(self):
        print('Axe')


class AxeGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return AxeReward()


if __name__ == '__main__':
    lst = [GoldGenerator(), GemGenerator(), AxeGenerator(), AppleGenerator()]
    for item in range(20):
        choice(lst).open_reward()
