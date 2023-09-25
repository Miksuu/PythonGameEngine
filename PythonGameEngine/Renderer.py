from OpenGL.GL import *

class Renderer:
    def __init__(self, color, pointSize):
        self.color = color
        self.pointSize = pointSize

    def drawRectangle(self, position):
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
        
    def drawTriangle():
        # Define the vertex array
        vertices = [0.0, 1.0,
                   -1.0, -1.0,
                    1.0, -1.0]
    
        # Enable vertex array and specify its data
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(2, GL_FLOAT, 0, vertices)
    
        # Draw the triangle
        glDrawArrays(GL_TRIANGLES, 0, 3)
    
        # Disable vertex array
        glDisableClientState(GL_VERTEX_ARRAY)   
