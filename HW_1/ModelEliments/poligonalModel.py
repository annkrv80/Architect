from typing import List

from HW_1.ModelEliments.texture import Texture
from HW_1.ModelEliments.poligon import Poligon, Point3D


class PoligonalModel:
    def __init__(self, textures: List[Texture]):
        self.textures = textures
        self.poligons: List[Poligon] = []
        self.poligons.append(Poligon(Point3D()))

