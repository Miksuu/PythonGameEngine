from OpenGL.GL import *

class Shader:
    def __init__(self, color):
        self.shader = self.initialize()
        self.color = color

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
    
        # Fragment Shader
        fragmentShaderSource = """
        #version 330 core
        out vec4 FragColor;
        void main()
        {
            FragColor = vec4(0.9f, 0.2f, 0.2f, 1f);
        }
        """
    
        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, fragmentShaderSource)
        glCompileShader(fragment_shader)
    
        # Check for shader compile errors
        if not glGetShaderiv(fragment_shader, GL_COMPILE_STATUS):
            print("ERROR: SHADER FRAGMENT COMPILATION_FAILED")
            return None
    
        # Link shaders
        shaderProgram = glCreateProgram()
        glAttachShader(shaderProgram, vertexShader)
        glAttachShader(shaderProgram, fragment_shader)
        glLinkProgram(shaderProgram)
    
        # Check for linking errors
        if not glGetProgramiv(shaderProgram, GL_LINK_STATUS):
            print("ERROR: SHADER PROGRAMLINKING_FAILED")
            return None
    
        return shaderProgram

    def setShaderUniforms(self):
        colorLocation = glGetUniformLocation(self.shader, "objectColor")
        glUseProgram(self.shader) # Needed to call this before
        glUniform3fv(colorLocation, 1, self.color)