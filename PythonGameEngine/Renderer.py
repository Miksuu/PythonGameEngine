from OpenGL.GL import *

class Renderer:
    def __init__(self, color, pointSize):
        self.color = color
        self.pointSize = pointSize

    #def render(self, position):
        # Existing rendering code for points
        # ...

    def drawRectangle(self, position):
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
