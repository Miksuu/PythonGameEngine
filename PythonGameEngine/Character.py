from GameObject import GameObject
from Vector2 import Vector2
from Camera import Camera

class Character(GameObject):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.movementSpeed = 0.01
        
        self.camera = Camera()
        
    def update(self):
        super().update()
        self.position += self.velocity
        
    def handleGameLoop(self):
        super().handleGameLoop()
