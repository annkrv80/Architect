from abc import ABC


class IModelChanger(ABC):
    def notifyChange(self, sender):
        pass