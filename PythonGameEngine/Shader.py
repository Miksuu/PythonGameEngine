from OpenGL.GL import *
from FileManager import FileManager

import ctypes

class Shader:
    def __init__(self, assetName):
        self.assetName = assetName
        # self.color = (0,0,0)
        self.shader = self.initialize()
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
    
    # def setShaderUniforms(self):
    #     colorLocation = glGetUniformLocation(self.shader, "objectColor")
    #     glUseProgram(self.shader)
    #     colorArray = (ctypes.c_float * len(self.color))(*self.color)
    #     glUniform3fv(colorLocation, 1, colorArray)