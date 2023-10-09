from abc import ABC


class IModelChangeObserver (ABC):
    def applyUpdateModel(self):
        pass

