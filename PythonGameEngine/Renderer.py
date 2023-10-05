from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*

from Camera import Camera
from Shader import Shader
from FileManager import FileManager

class Renderer:
    def __init__(self, color, camera, gameObjectName):
        # Search the asset and assign it to the class
        assetNameToSearchFor = "Assets/" + gameObjectName + "/vboData.py"
        self.playerAsset = FileManager(assetNameToSearchFor)
        self.playerAsset.readImportlib()
        
        # Assign vbo array from the file
        self.vboArray = self.playerAsset.module.vbo
        self.originalVertices = self.vboArray.copy()
        self.vbo = self.initializeVboData()
        
        #self.shaderArray = self.playerAsset.module.shader
        if camera != None:
            self.camera = camera
        
        self.debugColor = [1, 1, 0.5]

        self.shader = Shader(color, gameObjectName);               
        
    def initializeVboData(self):
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, len(self.vboArray) * 4, (ctypes.c_float * len(self.vboArray))(*self.vboArray), GL_STATIC_DRAW)
        return vbo
        
    def drawAsset(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        # Specify the layout of the vertex data
        glEnableVertexAttribArray(0)
        
        # Change to sizeof(7 * len(data_ ))
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, ctypes.c_void_p(0))

        # Draw the rectangle using two triangles
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4)

    def updateVertexData(self, position):
        #print(f"Updating with position: ({position.x}, {position.y})")        

        self.vboArray = self.originalVertices.copy()

        # Make sure the length of vertexData is a multiple of 2 for x, y coordinates
        if len(self.vboArray) % 2 != 0:
            raise ValueError("Invalid length for vertexData")

        # Update the vertex data based on the position
        for i in range(0, len(self.vboArray), 2):
            self.vboArray[i] += position.x
            self.vboArray[i+1] += position.y

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