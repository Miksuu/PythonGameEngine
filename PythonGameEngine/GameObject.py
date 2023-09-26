from turtle import position, update
from Renderer import Renderer
from Vector2 import Vector2

# Game class definitions
from InputManager import InputManager

class GameObject:
    def __init__(self, position, color, pointSize, speed, camera):
        self.position = Vector2(position.x, position.y)
        self.color = color
        self.pointSize = pointSize
        self.speed = speed

        # Add input to the player only
        if camera is None:
            pass
        else:
            self.inputManager = InputManager(self, camera)

        self.renderer = Renderer(color, pointSize, camera)
        
    def handleGameLoop(self):
        self.renderer.drawRectangle(self.position)
        coordinates_text = f"({self.position.x}, {self.position.y})"
        self.renderer.drawText(self.position, coordinates_text)
