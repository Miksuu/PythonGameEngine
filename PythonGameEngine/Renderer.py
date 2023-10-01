from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*

from Camera import Camera

class Renderer:
    def __init__(self, vertices, color, camera):
        self.vertices = vertices
        self.camera = camera
        self.color = color
        
        self.vbo = self.initializeVboData(vertices)

    def drawRectangle(self, position):
        # Apply camera transformations
        glTranslatef(-self.camera.position.x, -self.camera.position.y, 0)        

        # Set the color
        glColor3f(self.color[0], self.color[1], self.color[2])
        
        # Define the vertex array
        # vertices = [-0.1 + position.x, -0.2 + position.y,
        #              0.1 + position.x, -0.2 + position.y,
        #              0.1 + position.x,  0.2 + position.y,
        #             -0.1 + position.x,  0.2 + position.y]
        
        indices = [0, 1, 2, 3]
        
        # Enable vertex array and specify its data
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(2, GL_FLOAT, 0, self.vbo)
        glDrawElements(GL_QUADS, len(indices), GL_UNSIGNED_BYTE, indices)
        
        # Disable vertex array
        glDisableClientState(GL_VERTEX_ARRAY)
        
    def initializeVboData(self, vertices):
        # Set the color
        #glColor3f(self.color[0], self.color[1], self.color[2])        

        # # Define the vertex array
        # vertices = [0.0, 0.01,
        #            -0.01, -0.01,
        #             0.01, -0.01]
    
        # # Enable vertex array and specify its data
        # glEnableClientState(GL_VERTEX_ARRAY)
        # glVertexPointer(2, GL_FLOAT, 0, vertices)
    
        # # Draw the triangle
        # glDrawArrays(GL_TRIANGLES, 0, 3)
    
        # # Disable vertex array
        # glDisableClientState(GL_VERTEX_ARRAY)

        # Create a new VBO
        vbo = glGenBuffers(1)
        # Bind the VBO
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        
        # Load vertex data into the VBO
        glBufferData(GL_ARRAY_BUFFER, len(vertices)*4, (ctypes.c_float * len(vertices))(*vertices), GL_STATIC_DRAW)
    
        return vbo

    def drawVboTriangle(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        
        # Specify the layout of the vertex data
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))

        # Draw the triangle
        glDrawArrays(GL_TRIANGLES, 0, 3)

    def updateTriangleVertexData(self, position):
        # Make sure the length of triangleVertexData is a multiple of 2 for x, y coordinates
        if len(self.vertices) % 2 != 0:
            raise ValueError("Invalid length for triangleVertexData")
    
        # Update the triangle vertex data based on the position
        for i in range(0, len(self.vertices), 2):
            self.vertices[i] += position.x  # Update x-coordinate
            self.vertices[i+1] += position.y  # Update y-coordinate
            
    #Debugging tools, such as drawing the coordinates
    def setTextColor(self, color):
        glColor3f(color[0], color[1], color[2])

    def resetColor(self):
        glColor3f(self.color[0], self.color[1], self.color[2])

    def drawText(self, name , position, text):
        glRasterPos2f(position.x, position.y)
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))