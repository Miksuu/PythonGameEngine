from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

# Engine components
from GameObject import GameObject
from GameObjectManager import GameObjectManager
from Vector2 import Vector2

# Game class definitions
from InputManager import InputManager

gameObjectManager = GameObjectManager()
# Create a red point as a game object
# x, y positions as Vector2, color, pointSize, speed
player = GameObject(Vector2(0.1, 0.2), (1.0, 0.0, 0.0), 10.0, 0.1)

# Add input to the player
inputManager = InputManager(player)

gameObjectManager.addObject(player)

def main():
    print("Starting...")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow(b'test')
    glutDisplayFunc(plotpoints)
    init()
    
    glutKeyboardFunc(keyboard)

    glutMainLoop()
    print("Ending...")

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #drawRectangle()
    gameObjectManager.handleGameLoop()
    glutSwapBuffers()
    glFlush()
    
# def drawTriangle():
#     # Define the vertex array
#     vertices = [0.0, 1.0,
#                -1.0, -1.0,
#                 1.0, -1.0]
    
#     # Enable vertex array and specify its data
#     glEnableClientState(GL_VERTEX_ARRAY)
#     glVertexPointer(2, GL_FLOAT, 0, vertices)
    
#     # Draw the triangle
#     glDrawArrays(GL_TRIANGLES, 0, 3)
    
#     # Disable vertex array
#     glDisableClientState(GL_VERTEX_ARRAY)    

def keyboard(key, x, y):
    inputManager.move(key)

main()