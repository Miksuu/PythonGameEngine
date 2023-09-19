from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

class InputManager:
    def __init__(self, objectToControl):
        self.objectToControl = objectToControl
        
    def move(self, key):
    # Store the object's current position before moving
    # prev_object_x, prev_object_y = object_x, object_y
    
        if ord(key) == ord('w'):  # Move Up
            self.objectToControl.y += 0.1
        elif ord(key) == ord('s'):  # Move Down
            objectToControl.y -= 0.1
        elif ord(key) == ord('a'):  # Move Left
            objectToControl.x -= 0.1
        elif ord(key) == ord('d'):  # Move Right
            objectToControl.x += 0.1
        
        # if check_collision():
        #     print("Collision detected!")
        #     # Revert movement
        #     object_x, object_y = prev_object_x, prev_object_y

        if ord(key) == 27:  # ESC key
            print("Exiting...")
            glutLeaveMainLoop()
        glutPostRedisplay()