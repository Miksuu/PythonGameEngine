import time
from Character import Character
from Gun import Gun
from Vector2 import Vector2
from Renderer import Renderer

class AI(Character):
    def __init__(self, name, transform):
        super().__init__(name, transform)
        self.equipped_gun = Gun("Pistol", 10)
        
        self.lastShootTime = 0
        self.shootInterval = 2
        
        self.renderer = Renderer(None, name, transform)
        
    def update(self):
        super().update()
        
    def automaticShooting(self, gameObjectManager):
        currentTime = time.time()
        if currentTime - self.lastShootTime >= self.shootInterval:
            x, y = 1, 1  # Dummy target coordinates for now
            self.attack(x, y, gameObjectManager)
            self.lastShootTime = currentTime