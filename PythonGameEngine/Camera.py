from Vector2 import Vector2

class Camera:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.zoom = 1.0
    
    def updateOrientation(self, mouseX, mouseY):
        print(f"Updating camera orientation based on mouse coordinates: ({mouseX}, {mouseY})")
        # Update camera orientation based on mouse input
        # For demonstration, simply set the position to the mouse coordinates
        self.position = Vector2(mouseX, mouseY)
