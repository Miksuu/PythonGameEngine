from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*

from Camera import Camera

class Renderer:
    def __init__(self, color, pointSize, camera):
        self.camera = camera
        self.color = color
        self.pointSize = pointSize

    def drawRectangle(self, position):
        # Apply camera transformations
        glTranslatef(-self.camera.position.x, -self.camera.position.y, 0)        

        # Set the color
        glColor3f(self.color[0], self.color[1], self.color[2])
        
        # Define the vertex array
        vertices = [-0.1 + position.x, -0.2 + position.y,
                     0.1 + position.x, -0.2 + position.y,
                     0.1 + position.x,  0.2 + position.y,
                    -0.1 + position.x,  0.2 + position.y]
        
        indices = [0, 1, 2, 3]
        
        # Enable vertex array and specify its data
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(2, GL_FLOAT, 0, vertices)
        glDrawElements(GL_QUADS, len(indices), GL_UNSIGNED_BYTE, indices)
        
        # Disable vertex array
        glDisableClientState(GL_VERTEX_ARRAY)
        
    def drawTriangle(self):
        # Set the color
        glColor3f(self.color[0], self.color[1], self.color[2])        

        # Define the vertex array
        vertices = [0.0, 0.01,
                   -0.01, -0.01,
                    0.01, -0.01]
    
        # Enable vertex array and specify its data
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(2, GL_FLOAT, 0, vertices)
    
        # Draw the triangle
        glDrawArrays(GL_TRIANGLES, 0, 3)
    
        # Disable vertex array
        glDisableClientState(GL_VERTEX_ARRAY)   

    #Debugging tools
    def drawText(self, position, text):
        glRasterPos2f(position.x, position.y)
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))