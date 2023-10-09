from typing import List

from HW_1.ModelEliments.poligonalModel import PoligonalModel
from HW_1.ModelEliments.flash import Flash
from HW_1.ModelEliments.camera import Camera


class Scene:
    def __init__(self, id: int, models: List[PoligonalModel], flashes: List[Flash], camera: List[Camera]):
        self.id = id
        if len(models) > 0:
            self.models = models
        else:
            f'Должна быть одна модель'
        self.flashes = flashes
        if len(camera) > 0:
            self.camera = camera
        else:
            f'Должна быть одна модель'



    def method1(self):
        return self

    def method2(self):
        return self