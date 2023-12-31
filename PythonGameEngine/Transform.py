# Generated by GPT

from Vector2 import Vector2
from Quaternion import Quaternion

class Transform:
    def __init__(self, position=Vector2(0,0), rotation=Quaternion(), scale=Vector2(1, 1)):
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def __str__(self):
        return f"Transform(Position={self.position}, Rotation={self.rotation}, Scale={self.scale})"

    def __repr__(self):
        return self.__str__()
