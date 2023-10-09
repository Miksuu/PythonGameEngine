from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

from Camera import Camera
from Vector2 import Vector2

class InputManager:
    def __init__(self, objectToControl, camera):
        self.objectToControl = objectToControl
        self.camera = camera
        self.keys = {}  # Initialize an empty dictionary to hold key states

    def keyDown(self, key):
        self.keys[ord(key)] = True  # Set the state to True when the key is down

    def keyUp(self, key):
        self.keys[ord(key)] = False

        if ord(key) == ord('w') or ord(key) == ord('s'):
            self.objectToControl.velocity.y = 0
        if ord(key) == ord('a') or ord(key) == ord('d'):
            self.objectToControl.velocity.x = 0

    def update(self):
        # Check the state of each key and update velocity accordingly
        if self.keys.get(ord('w'), False):
            self.objectToControl.velocity.y = 1 * self.objectToControl.movementSpeed
        if self.keys.get(ord('a'), False):
            self.objectToControl.velocity.x = -1 * self.objectToControl.movementSpeed
        if self.keys.get(ord('s'), False):
            self.objectToControl.velocity.y = -1 * self.objectToControl.movementSpeed
        if self.keys.get(ord('d'), False):
            self.objectToControl.velocity.x = 1 * self.objectToControl.movementSpeed
            
        #print(self.objectToControl.__repr__)

    def handleMouseMovement(self, x, y):
        self.camera.updateOrientation(x, y, self.objectToControl)
        
    def __repr__(self):
        return f"InputManager(Keys: {self.keys})"
