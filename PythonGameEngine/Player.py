from GameObject import GameObject
from Renderer import Renderer
from Vector2 import Vector2
from Camera import Camera

# Game class definitions
from InputManager import InputManager

class Player(GameObject):
    def __init__(self, name, position):
        super().__init__(name, position)
        
        self.camera = Camera()
        self.inputManager = InputManager(self, self.camera)
        self.renderer = Renderer(self.camera, name)