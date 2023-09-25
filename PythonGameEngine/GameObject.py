from turtle import position
from Renderer import Renderer
from Vector2 import Vector2

class GameObject:
    def __init__(self, position, color, pointSize, speed):
        self.position = Vector2(position.x, position.y)
        self.color = color
        self.pointSize = pointSize
        self.speed = speed        

        self.renderer = Renderer(color, pointSize)
        
    def handleGameLoop(self):
        #self.renderer.render(self.position)
        self.renderer.drawRectangle(self.position)
        