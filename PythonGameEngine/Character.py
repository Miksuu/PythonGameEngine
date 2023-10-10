from GameObject import GameObject
from Vector2 import Vector2
from Camera import Camera
from Gun import Gun

class Character(GameObject):
    def __init__(self, name, transform):
        super().__init__(name, transform)
        self.movementSpeed = 0.01
        
        self.camera = Camera()
        
    def update(self):
        super().update()
        self.transform.position += self.velocity
        
    def handleGameLoop(self):
        super().handleGameLoop()

    def equipGun(self, gun):
        self.equipped_gun = gun

    def attack(self, x, y, gameObjectManager):
        if hasattr(self, 'equipped_gun'):
            self.equipped_gun.shoot(self.transform, x, y, gameObjectManager)
