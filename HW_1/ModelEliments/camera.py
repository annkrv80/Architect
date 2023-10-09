from HW_1.ModelEliments.flash import Point3D, Angle3d


class Camera:
    def __init__(self):
        self.location: Point3D
        self.angle: Angle3d

    def rotate(self, angle: Angle3d):
        pass

    def move(self, location: Point3D):
        pass
