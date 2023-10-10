from Character import Character
from GameObject import GameObject
from Renderer import Renderer
from Vector2 import Vector2
from Camera import Camera

from InputManager import InputManager

class Player(Character):
    def __init__(self, name, transform):
        super().__init__(name, transform)
        self.movementSpeed = 0.01
        
        self.camera = Camera()
        self.inputManager = InputManager(self, self.camera)
        self.renderer = Renderer(self.camera, name, transform)

    def update(self):
        self.transform.position += self.velocity