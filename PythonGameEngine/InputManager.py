from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

from Camera import Camera

class InputManager:
    def __init__(self, objectToControl, camera):
        self.objectToControl = objectToControl
        self.camera = camera
        
    def move(self, key):    
        if ord(key) == ord('w'):  # Move Up
            self.objectToControl.position.y += 0.1
        elif ord(key) == ord('s'):  # Move Down
            self.objectToControl.position.y -= 0.1
        elif ord(key) == ord('a'):  # Move Left
            self.objectToControl.position.x -= 0.1
        elif ord(key) == ord('d'):  # Move Right
            self.objectToControl.position.x += 0.1

        if ord(key) == 27:  # ESC key
            print("Exiting...")
            glutLeaveMainLoop()
        glutPostRedisplay()
    
    def handleMouseMovement(self, x, y):
        self.camera.updateOrientation(x, y)