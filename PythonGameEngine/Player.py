from Character import Character
from GameObject import GameObject
from Renderer import Renderer
from Vector2 import Vector2
from Camera import Camera

from InputManager import InputManager

class Player(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.movementSpeed = 0.01
        
        self.camera = Camera()
        self.inputManager = InputManager(self, self.camera)
        self.renderer = Renderer(self.camera, name, position)

    def update(self):
        self.position += self.velocity