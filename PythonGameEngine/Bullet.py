from GameObject import GameObject
from Renderer import Renderer
from Vector2 import Vector2

class Bullet(GameObject):
    def __init__(self, name, position, mouseX, mouseY):
        super().__init__(name, position)
        
        # Debugging
        print("Debug Position: ", position.x, " | ", position.y)
        
        # Calculate the mouse offsets
        offsetX = (mouseX - 600) * 0.001
        offsetY = (mouseY - 600) * 0.001

        print("Debug calculated offset: ", offsetX, " | ", offsetY)

        # Compute the direction vector
        direction = Vector2(mouseX - 600, 600 - mouseY) - position
        print("Debug Direction: ", direction.x, " | ", direction.y)
        
        self.velocity = direction.normalize() * 0.01
        print("Debug Velocity: ", self.velocity.x, " | ", self.velocity.y)
        
        self.renderer = Renderer(None, name, position)