from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*

from Camera import Camera
from Shader import Shader

class Renderer:
    def __init__(self, vertices, color, camera):
        self.originalVertices = vertices.copy()
        self.vertices = vertices
        
        if camera != None:
            self.camera = camera
        
        self.debugColor = [1, 1, 0.5]

        self.shader = Shader(color);
        
        self.vbo = self.initializeVboData(vertices)
        
    def initializeVboData(self, vertices):
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, len(vertices) * 4, (ctypes.c_float * len(vertices))(*vertices), GL_STATIC_DRAW)
        return vbo
        
    def drawVboRectangle(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        # Specify the layout of the vertex data
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))

        # Draw the rectangle using two triangles
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4)

    def updateVertexData(self, position):
        #print(f"Updating with position: ({position.x}, {position.y})")        

        self.vertices = self.originalVertices.copy()

        # Make sure the length of vertexData is a multiple of 2 for x, y coordinates
        if len(self.vertices) % 2 != 0:
            raise ValueError("Invalid length for vertexData")

        # Update the vertex data based on the position
        for i in range(0, len(self.vertices), 2):
            self.vertices[i] += position.x
            self.vertices[i+1] += position.y

        # Update the VBO
        self.updateVbo()

    def updateVbo(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0, len(self.vertices) * 4, (ctypes.c_float * len(self.vertices))(*self.vertices))
            
    #Debugging tools, such as drawing the coordinates
    def setTextColor(self):
        glColor3f(self.debugColor[0], self.debugColor[1], self.debugColor[2])

    def resetColor(self):
        glColor3f(self.debugColor[0], self.debugColor[1], self.debugColor[2])

    def drawText(self, name , position, text):
        glRasterPos2f(position.x, position.y)
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
