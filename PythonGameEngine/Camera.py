from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

from Vector2 import Vector2

class Camera:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.zoom = 1.0
    
    def updateOrientation(self, mouseX, mouseY, gameObject):
        #print(f"GameObject position before camera update: {gameObject.position.x} | {gameObject.position.y}")
        #print(f"Updating camera orientation based on mouse coordinates: ({mouseX}, {mouseY})")
        #print(f"Camera position before update: {self.position.x} | {self.position.y}")
    
        scalingFactor = 0.1
        scaledMouseX = mouseX * scalingFactor
        scaledMouseY = mouseY * scalingFactor
    
        newCameraX = gameObject.position.x + scaledMouseX * 0.01
        newCameraY = gameObject.position.y + scaledMouseY * 0.01
    
        offsetX = (mouseX - 600) * 0.001  # Assuming 1200x1200 window, refactor this later
        offsetY = (mouseY - 600) * 0.001
    
        self.position.x = gameObject.position.x + offsetX
        self.position.y = gameObject.position.y + offsetY
        
        #print(f"Camera position after update: {self.position.x} | {self.position.y}")
        #print(f"GameObject position after camera update: {gameObject.position.x} | {gameObject.position.y}")
