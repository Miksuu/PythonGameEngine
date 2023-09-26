from turtle import position, update
from Renderer import Renderer
from Vector2 import Vector2
from GameObject import GameObject

class TriangleGameObject(GameObject):
    def __init__(self, name , position, color, pointSize, speed, velocity):
        super().__init__(name, position, color, pointSize, speed, None)
        self.velocity = velocity
        
    # Overridden method
    def handleGameLoop(self):
        #print(str(self.position.x) + " | " + str(self.position.y))
        self.update()
        self.renderer.drawTriangle()

    def update(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
