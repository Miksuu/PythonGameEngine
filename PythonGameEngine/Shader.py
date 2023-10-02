from OpenGL.GL import *

import ctypes

class Shader:
    def __init__(self, color):
        self.color = color
        self.shader = self.initialize()

    def initialize(self):
        # Vertex Shader
        vertexShaderSource = """
        #version 330 core
        layout (location = 0) in vec3 aPos;
        void main()
        {
            gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
        }
        """
    
        vertexShader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertexShader, vertexShaderSource)
        glCompileShader(vertexShader)
    
        # Check for shader compile errors
        if not glGetShaderiv(vertexShader, GL_COMPILE_STATUS):
            print("ERROR: SHADER VERTEX COMPILATION_FAILED")
            return None
    
        fragmentShaderSource = f"""
        #version 330 core
        out vec4 FragColor;
        void main()
        {{
            FragColor = vec4({self.color[0]}f, {self.color[1]}f, {self.color[2]}f, 1f);
        }}
        """
    
        fragmentShader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragmentShader, fragmentShaderSource)
        glCompileShader(fragmentShader)
    
        # Check for shader compile errors
        if not glGetShaderiv(fragmentShader, GL_COMPILE_STATUS):
            print("ERROR: SHADER FRAGMENT COMPILATION_FAILED")
            return None
    
        # Link shaders
        shader = glCreateProgram()
        glAttachShader(shader, vertexShader)
        glAttachShader(shader, fragmentShader)
        glLinkProgram(shader)
    
        # Check for linking errors
        if not glGetProgramiv(shader, GL_LINK_STATUS):
            print("ERROR: SHADER PROGRAMLINKING_FAILED")
            return None
    
        return shader

    def setShaderUniforms(self):
        colorLocation = glGetUniformLocation(self.shader, "objectColor")
        glUseProgram(self.shader)
        colorArray = (ctypes.c_float * len(self.color))(*self.color)
        glUniform3fv(colorLocation, 1, colorArray)