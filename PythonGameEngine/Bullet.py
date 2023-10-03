from GameObject import GameObject
from Renderer import Renderer
from Vector2 import Vector2

class Bullet(GameObject):
    def __init__(self, name, position, color, mouseX, mouseY):
        super().__init__(name, position, color, 0.1)
        
        offsetX = (mouseX - 600) * 0.001  # Assuming 1200x1200 window, refactor this later
        offsetY = (mouseY - 600) * 0.001

        print("POS: ", position.x, " | ", position.y)
        print("calculated offset: ", offsetX, " | ", offsetY)

        self.velocity = Vector2(offsetX, -offsetY).normalize() * 0.01 ## temp way to set the speed
        #print("finalVelocity: " , self.velocity.x, " | ", self.velocity.y)
        self.renderer = Renderer(color, None, name)