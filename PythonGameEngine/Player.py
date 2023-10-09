from GameObject import GameObject
from Renderer import Renderer
from Vector2 import Vector2
from Camera import Camera

# Game class definitions
from InputManager import InputManager

class Player(GameObject):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.movementSpeed = 0.01
        
        self.camera = Camera()
        self.inputManager = InputManager(self, self.camera)
        self.renderer = Renderer(self.camera, name)

    def update(self):
        self.position += self.velocity

    def __repr__(self):
        return f"Player(Position: {self.position.x}, Velocity: {self.velocity.x}, MovementSpeed: {self.movementSpeed})"