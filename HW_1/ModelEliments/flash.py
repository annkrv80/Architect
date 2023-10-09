from HW_1.ModelEliments.poligon import Point3D


class Angle3d:
    pass


class Color:
    pass


class Flash:
    def __init__(self):
        self.location: Point3D
        self.angle: Angle3d
        self.color: Color
        self.power: float

    def rotate(self, angle: Angle3d):
        pass

    def move(self, location: Point3D):
        pass

