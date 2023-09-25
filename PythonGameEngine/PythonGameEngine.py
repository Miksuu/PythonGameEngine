from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

# Engine components
from Camera import Camera
from GameObject import GameObject
from GameObjectManager import GameObjectManager
from Vector2 import Vector2

gameObjectManager = GameObjectManager()

camera = Camera()

# x, y positions as Vector2, color, pointSize, speed, camera ref
player = GameObject(Vector2(0.1, 0.2), (1.0, 0.5, 0.0), 10.0, 0.1, camera)

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
    
    # Add this line to handle mouse movement
    glutMotionFunc(mouseMotion)
    
    glutMainLoop()
    print("Ending...")

# Implement this new function to handle mouse motion
def mouseMotion(x, y):
    # Call the handleMouseMovement method from InputManager
    player.inputManager.handleMouseMovement(x, y)

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gameObjectManager.handleGameLoop()
    glutSwapBuffers()
    glFlush() 

def keyboard(key, x, y):
    player.inputManager.move(key)

main()