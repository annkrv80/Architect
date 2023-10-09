from typing import List


from HW_1.ModelEliments.poligonalModel import PoligonalModel
from HW_1.ModelEliments.flash import Flash
from HW_1.ModelEliments.camera import Camera
from HW_1.ModelEliments.scene import Scene
from HW_1.InMemoryModel.iModelChanger import  IModelChanger


class ModelStore:

    def __init__(self):
        self.models: List[PoligonalModel] = []
        self.scenes: List[Scene] = []
        self.flashes: List[Flash] = []
        self.cameras: List[Camera] = []
        self.changeObservers = []

        self.models.append(PoligonalModel())
        self.flashes.append(Flash())
        self.cameras.append(Camera())
        self.scenes.append(Scene(0, self.models, self.flashes, self.cameras))

    def getScena(self, id: int):
        for i in range(len(self.scenes)):
            if self.scenes[i].id == id:
                return self.scenes[i]
        return None

    def notifyChange(self, sender: IModelChanger):
        pass

