from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

from Vector2 import Vector2

class Renderer:
    def __init__(self, color, pointSize):
        self.worldObjects = []
        self.color = color
        self.pointSize = pointSize
        
    def render(self, position):
        glColor3f(*self.color)
        glPointSize(self.pointSize)
        glBegin(GL_POINTS)
        glVertex2f(position.x, position.y)
        glEnd()