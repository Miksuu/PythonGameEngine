from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*

from Camera import Camera
from Shader import Shader
from FileManager import FileManager

from array import array
from ctypes import create_string_buffer
from struct import unpack

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
        self.vbo = self.initializeVboData()

        if camera != None:
            self.camera = camera
        
        self.debugColor = [1, 1, 0.5]

    def initializeVboData(self):
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vboArray.buffer_info()[1] * self.vboArray.itemsize, self.vboArray.tobytes(), GL_STATIC_DRAW)

        return vbo

    def drawAsset(self):
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 28, ctypes.c_void_p(0))
        glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 28, ctypes.c_void_p(12))
        glDrawArrays(GL_TRIANGLES, 0, 3)

    def updateVertexData(self, position):
        self.updateVbo(position)

    def updateVbo(self, position):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
    
        for i in range(0, len(self.vboArray), 7):
            self.vboArray[i] += position.x
            self.vboArray[i+1] += position.y
            print(f"Updated self.vboArray: {self.vboArray}")

        position.x = 0
        position.y = 0
            
        updatedData = array('f', self.vboArray)
        glBufferData(GL_ARRAY_BUFFER, len(updatedData) * 4, updatedData.tobytes(), GL_STATIC_DRAW)
    
    def __repr__(self):
        return f"Renderer(VBO: {self.vbo}, VBOArray: {self.vboArray})"
            
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