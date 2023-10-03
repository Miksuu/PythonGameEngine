from GameObject import GameObject
from Renderer import Renderer
from Vector2 import Vector2
from Camera import Camera

# Game class definitions
from InputManager import InputManager

class Player(GameObject):
    def __init__(self, name, assetData, position, color, speed):
        super().__init__(name, assetData, position, color, speed)
        
        self.camera = Camera()
        self.inputManager = InputManager(self, self.camera)
        self.renderer = Renderer(assetData, self.color, self.camera)

    # Add Player-specific methods here (work in progress)
    def move(self):
        pass