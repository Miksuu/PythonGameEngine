from GameObject import GameObject
from Renderer import Renderer
from Vector2 import Vector2

class Bullet(GameObject):
    def __init__(self, name, vertices, position, color, speed):
        super().__init__(name, vertices, position, color, speed)
        
        self.velocity = Vector2(0.005, 0.005)  # Add a velocity vector for the projectile
        self.renderer = Renderer(vertices, color, None)