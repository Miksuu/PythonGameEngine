from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

class GameObject:
    def __init__(self, x, y, color, point_size):
        self.x = x
        self.y = y
        self.color = color
        self.point_size = point_size

    def render(self):
        glColor3f(*self.color)
        glPointSize(self.point_size)
        glBegin(GL_POINTS)
        glVertex2f(self.x, self.y)
        glEnd()