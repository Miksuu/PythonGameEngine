from OpenGL.GL import *
from FileManager import FileManager
import ctypes
import numpy as np
from PIL import Image

class Shader:
    def __init__(self, assetName):
        self.assetName = assetName
        self.shader = self.initialize()

        self.initTextures()

        glUseProgram(self.shader)

    def initialize(self):
        pathToSearchFor = "Assets/" + self.assetName + "/"

        vertexShader = self.initShader(pathToSearchFor, "shader.vert", GL_VERTEX_SHADER)
        fragmentShader = self.initShader(pathToSearchFor, "shader.frag", GL_FRAGMENT_SHADER)
        
        shader = glCreateProgram()
        glAttachShader(shader, vertexShader)
        glAttachShader(shader, fragmentShader)
        glLinkProgram(shader)
    
        if not glGetProgramiv(shader, GL_LINK_STATUS):
            print("ERROR: SHADER PROGRAMLINKING_FAILED")
            return None
    
        return shader

    def initShader(self, pathToSearchFor, postFix, shaderType):
        shaderSourceFile = FileManager(pathToSearchFor + postFix)
        shaderSource = shaderSourceFile.readAsString()     

        shader = glCreateShader(shaderType)
        glShaderSource(shader, shaderSource)
        glCompileShader(shader)
    
        if not glGetShaderiv(shader, GL_COMPILE_STATUS):
            print("ERROR: SHADER COMPILATION_FAILED ON: ", str(shaderType))
            return None    
        
        return shader
    
    def initTextures(self):
        texturePath = "Assets/Textures/wall.png"

        texture = self.loadTexture(texturePath)
        glBindTexture(GL_TEXTURE_2D, texture)

        #glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), ctypes.c_void_p(0))
        #glEnableVertexAttribArray(0)
        #glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), ctypes.c_void_p(12))
        #glEnableVertexAttribArray(1)

    def loadTexture(self, path):
        image = Image.open(path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = np.array(list(image.getdata()), np.uint8)
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
        return texture

    # def setShaderUniforms(self):
    #     colorLocation = glGetUniformLocation(self.shader, "objectColor")
    #     glUseProgram(self.shader)
    #     colorArray = (ctypes.c_float * len(self.color))(*self.color)
    #     glUniform3fv(colorLocation, 1, colorArray)