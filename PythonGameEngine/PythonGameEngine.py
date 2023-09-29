from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

# Engine components
from Camera import Camera
from GameObject import GameObject
from TriangleGameObject import TriangleGameObject
from GameObjectManager import GameObjectManager
from Vector2 import Vector2
from WindowManagement import WindowManagement

gameObjectManager = GameObjectManager()
windowManagement = WindowManagement(gameObjectManager)

camera = Camera()

projectileCount = 0

# name, x, y positions as Vector2, color, speed, camera ref
player = GameObject("Player", Vector2(0.1, 0.2), (1.0, 0.5, 0.0), 0.1, camera)

gameObjectManager.addObject(player)

draggingMouse = False

def main():
    print("Starting...")
    windowManagement.setupWindow()
    
    glutKeyboardFunc(keyboard)
    
    # Lines to handle mouse movement
    glutMouseFunc(mouseButton)
    glutMotionFunc(mouseDrag)

    # Initialize VBO
    vbo = initializeVbo()

    # Initialize Shaders
    shaderProgram = initializeShaders()

    # Main game loop
    while True:
        print("Starting MAINLOOP")

        # Use the shader program
        glUseProgram(shaderProgram)

        # Bind the VBO
        glBindBuffer(GL_ARRAY_BUFFER, vbo)

        # Specify the layout of the vertex data
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))

        # Draw the triangle
        glDrawArrays(GL_TRIANGLES, 0, 3)

        # Run the GLUT mainloop
        glutMainLoop()
        
        gameObjectManager.handleGameLoop()

        print("Ending MAINLOOP")


    print("Ending...")

def mouseButton(button, state, x, y):
    global draggingMouse

    if state == GLUT_DOWN:
        # Dragging mouse, camera control
        if button == GLUT_RIGHT_BUTTON:
            draggingMouse = True
            ##recenterCamera()  # Re-center when the button is released

        # Shooting mechanics implementation
        if button == GLUT_LEFT_BUTTON:
            # x, y positions as Vector2, color, speed, camera ref, velocity
            projectilePosition = Vector2(player.position.x, player.position.y)
            projectileColor = (0.2, 1.0, 0.2);
            projectileVelocity = Vector2(0.05, 0.05)  # Add a velocity vector for the projectile

            projectile = TriangleGameObject("Bullet_" + str(projectileCount), projectilePosition, projectileColor, 0.1, projectileVelocity)
            gameObjectManager.addObject(projectile)
    else:
        draggingMouse = False

def mouseDrag(x, y):
    if draggingMouse:
        player.inputManager.handleMouseMovement(x, y)
        # Need to keep updating the position while mouse is on the movement
        glutPostRedisplay()

def recenterCamera():
    camera.position = player.position

def keyboard(key, x, y):
    player.inputManager.move(key)

# Initialize a VBO
def initializeVbo():
    # Create a new VBO
    vbo = glGenBuffers(1)
    # Bind the VBO
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    
    # Vertex data (x, y, coordinates)
    vertexData = [
        -0.5, -0.5,
         0.5, -0.5,
         0.0,  0.5,
    ]
    
    # Load vertex data into the VBO
    glBufferData(GL_ARRAY_BUFFER, len(vertexData)*4, (ctypes.c_float * len(vertexData))(*vertexData), GL_STATIC_DRAW)
    
    return vbo

# Initialize shaders
def initializeShaders():
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
        print("ERROR::SHADER::VERTEX::COMPILATION_FAILED")
        return None
    
    # Fragment Shader
    fragmentShaderSource = """
    #version 330 core
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
    }
    """
    
    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, fragmentShaderSource)
    glCompileShader(fragment_shader)
    
    # Check for shader compile errors
    if not glGetShaderiv(fragment_shader, GL_COMPILE_STATUS):
        print("ERROR::SHADER::FRAGMENT::COMPILATION_FAILED")
        return None
    
    # Link shaders
    shaderProgram = glCreateProgram()
    glAttachShader(shaderProgram, vertexShader)
    glAttachShader(shaderProgram, fragment_shader)
    glLinkProgram(shaderProgram)
    
    # Check for linking errors
    if not glGetProgramiv(shaderProgram, GL_LINK_STATUS):
        print("ERROR::SHADER::PROGRAM::LINKING_FAILED")
        return None
    
    return shaderProgram

main()
