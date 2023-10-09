from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

from Camera import Camera
from Vector2 import Vector2

class InputManager:
    def __init__(self, objectToControl, camera):
        self.keys = {}
        self.objectToControl = objectToControl
        
        self.camera = camera
        
    def keyDown(self, key):
        self.keys[key] = True

    def keyUp(self, key):
        self.keys[key] = False
    
    def move(self, key):
        direction = Vector2(0,0)        
        
        if self.keys.get('w', False):
            direction += Vector2(0, 1)
        if self.keys.get('a', False):
            direction += Vector2(-1, 0)
        if self.keys.get('s', False):
            direction += Vector2(0, -1)
        if self.keys.get('d', False):
            direction += Vector2(1, 0)

        if ord(key) == 27:  # ESC key
            print("Exiting...")
            glutLeaveMainLoop()
        glutPostRedisplay()

    def handleMouseMovement(self, x, y):
        self.camera.updateOrientation(x, y, self.objectToControl)
        
    def __repr__(self):
        return f"InputManager(Keys: {self.keys})"
    