from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*

from Camera import Camera
from Shader import Shader
from FileManager import FileManager

from array import array

class Renderer:
    def __init__(self, camera, gameObjectName):
        # Search the asset and assign it to the class
        assetNameToSearchFor = "Assets/" + gameObjectName + "/vboData.py"
        self.playerAsset = FileManager(assetNameToSearchFor)
        self.playerAsset.readImportlib()
        
        self.shader = Shader(gameObjectName);      

        # Assign vbo array from the file
        self.vboArray = self.playerAsset.module.shader
        self.vboArray = array('f', self.vboArray)
        #self.vboArray = self.originalVertices.copy()
        self.originalVertices = self.vboArray
        self.vbo = self.initializeVboData()
        
        #self.shaderArray = self.playerAsset.module.shader
        if camera != None:
            self.camera = camera
        
        self.debugColor = [1, 1, 0.5]

    def initializeVboData(self):
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)

        try:
            glBufferData(GL_ARRAY_BUFFER, self.vboArray.buffer_info()[1] * self.vboArray.itemsize, self.vboArray.tobytes(), GL_STATIC_DRAW)
        except Exception as e:
            print("Error:", str(e))

        return vbo

        
    def drawAsset(self):
        #glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        
        # Change to sizeof(7 * len(data_ ))
        #glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))

        # Enable vertex attributes
        glEnableVertexAttribArray(0)  # Position attribute at index 0
        glEnableVertexAttribArray(1)  # Color attribute at index 1

        # Bind the VBO
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        # Point to the data for the vertex attributes
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 28, ctypes.c_void_p(0))
        glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 28, ctypes.c_void_p(12))

        # Draw the triangle
        glDrawArrays(GL_TRIANGLES, 0, 3)  # Drawing triangles, starting from vertex 0, and using 3 vertices

        # Draw the rectangle using two triangles
        #glDrawArrays(GL_TRIANGLE_FAN, 0, 4)

    def updateVertexData(self, position):
        #print(f"Updating with position: ({position.x}, {position.y})")        

        #self.vboArray = self.originalVertices.copy()
        self.vboArray = self.originalVertices

        # Make sure the length of vertexData is a multiple of 2 for x, y coordinates
        # if len(self.vboArray) % 2 != 0:
        #     raise ValueError("Invalid length for vertexData")

        # print(len(self.vboArray))

        # for i in range(0, len(self.vboArray), 2):
        #     self.vboArray[i] += position.x
        #     self.vboArray[i+1] += position.y

        # Update the VBO
        self.updateVbo()

    def updateVbo(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0, len(self.vboArray) * 4, (ctypes.c_float * len(self.vboArray))(*self.vboArray))
            
    #Debugging tools, such as drawing the coordinates
    def setTextColor(self):
        glColor3f(self.debugColor[0], self.debugColor[1], self.debugColor[2])

    def resetColor(self):
        glColor3f(self.debugColor[0], self.debugColor[1], self.debugColor[2])

    def drawText(self, name, position, text):
        #print(position.x, " | ", position.y)
        # Check if the object's position is within the window
        # Refactor this later to move with the camera
        if position.x >= -1 and position.x <= 1 and position.y >= -1 and position.y <= 1:
            glRasterPos2f(position.x, position.y)
            for char in text:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        else:
            pass