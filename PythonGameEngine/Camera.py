from Vector2 import Vector2

class Camera:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.zoom = 1.0
    
    def updateOrientation(self, mouseX, mouseY):
        print(f"Updating camera orientation based on mouse coordinates: ({mouseX}, {mouseY})")
        print(f"Camera position before update: {self.position.x} | {self.position.y}")
        # Existing code for updating camera orientation
        print(f"Camera position after update: {self.position.x} | {self.position.y}")
        scaling_factor = 0.1
        scaled_mouseX = mouseX * scaling_factor
        scaled_mouseY = mouseY * scaling_factor
        # Update camera orientation based on scaled mouse coordinates
        self.position = Vector2(scaled_mouseX, scaled_mouseY)