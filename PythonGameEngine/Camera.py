from Vector2 import Vector2

class Camera:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.zoom = 1.0
    
    def updateOrientation(self, mouseX, mouseY, gameObject):
        print(f"GameObject position before camera update: {gameObject.position.x} | {gameObject.position.y}")
        print(f"Updating camera orientation based on mouse coordinates: ({mouseX}, {mouseY})")
        print(f"Camera position before update: {self.position.x} | {self.position.y}")
    
        # Calculate the scaled mouse coordinates
        scaling_factor = 0.1
        scaled_mouseX = mouseX * scaling_factor
        scaled_mouseY = mouseY * scaling_factor
    
        # Calculate new camera position based on GameObject's position and scaled mouse coordinates
        new_camera_x = gameObject.position.x + scaled_mouseX * 0.01  # added scaling for mouse influence
        new_camera_y = gameObject.position.y + scaled_mouseY * 0.01
    
        # Update the camera position
        self.position = Vector2(new_camera_x, new_camera_y)
    
        print(f"Camera position after update: {self.position.x} | {self.position.y}")
        print(f"GameObject position after camera update: {gameObject.position.x} | {gameObject.position.y}")
