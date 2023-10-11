from GameObject import GameObject
from Renderer import Renderer
from Vector2 import Vector2

class Bullet(GameObject):
    def __init__(self, name, transform, targetVec2):
        super().__init__(name, transform)

        # Compute the direction vector
        direction = Vector2(targetVec2.x - 600, 600 - targetVec2.y) - transform.position
        #print("Debug Direction: ", direction.x, " | ", direction.y)
        
        self.velocity = direction.normalize() * 0.01
        #projectile.velocity = Vector2(1, 1)  # Temp Setting the projectile to go with 1,1 velocity
        #print("Debug Velocity: ", self.velocity.x, " | ", self.velocity.y)

        print("bullet transform: ", transform.position.x, "|", transform.position.y, " | targetVec2: ", targetVec2.x, "|", targetVec2.y)
        
        self.renderer = Renderer(None, name, transform)
        
# OLD CLASS FOR THE BULLET TAKING IN THE MOUSE POSITION, DO NOT DELETE!!! (Unless player controlled bots idea discarded)
# class Bullet(GameObject):
#     def __init__(self, name, transform, mouseX, mouseY):
#         super().__init__(name, transform)
        
#         #print("Debug Position: ", position.x, " | ", position.y)
        
#         offsetX = (mouseX - 600) * 0.001
#         offsetY = (mouseY - 600) * 0.001
        
#         #print("Debug calculated offset: ", offsetX, " | ", offsetY)

#         # Compute the direction vector
#         direction = Vector2(mouseX - 600, 600 - mouseY) - transform.position
#         #print("Debug Direction: ", direction.x, " | ", direction.y)
        
#         self.velocity = direction.normalize() * 0.01
#         #print("Debug Velocity: ", self.velocity.x, " | ", self.velocity.y)
        
#         self.renderer = Renderer(None, name, transform)