from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*

from Camera import Camera

class Renderer:
    def __init__(self, vertices, color, camera):
        self.originalVertices = vertices.copy()
        self.vertices = vertices
        self.camera = camera
        self.color = color
        
        self.shaderProgram = self.initializeShaders()
        
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
            
    def setShaderUniforms(self):
        colorLocation = glGetUniformLocation(self.shaderProgram, "objectColor")
        glUseProgram(self.shaderProgram) # Needed to call this before
        glUniform3fv(colorLocation, 1, self.color)
        
    #Debugging tools, such as drawing the coordinates
    def setTextColor(self, color):
        glColor3f(color[0], color[1], color[2])

    def resetColor(self):
        glColor3f(self.color[0], self.color[1], self.color[2])

    def drawText(self, name , position, text):
        glRasterPos2f(position.x, position.y)
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
    def initializeShaders(self):
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