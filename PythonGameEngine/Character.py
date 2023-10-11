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
        self.equippedGun = gun

    def attack(self, targetVec2, gameObjectManager):
        if hasattr(self, 'equippedGun'):
            self.equippedGun.shoot(self.transform, targetVec2, gameObjectManager)
