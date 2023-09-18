from turtle import color
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

class Renderer:
    def __init__(self, color, pointSize):
        self.worldObjects = []
        self.color = color
        self.pointSize = pointSize
        
    def render(self, x, y):
        glColor3f(*self.color)
        glPointSize(self.pointSize)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()