import time
from Character import Character
from Gun import Gun
from Vector2 import Vector2
from Renderer import Renderer

class AI(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.equipped_gun = Gun("Pistol", 10)
        
        self.renderer = Renderer(None, name, position)
        
    def update(self):
        super().update()
        
    def automaticShooting(self, gameObjectManager):
        while True:
            x, y = 1, 1  # Dummy target coordinates for now
            self.attack(x, y, gameObjectManager)
            time.sleep(2)  # Temp, Shoots every 2 seconds
