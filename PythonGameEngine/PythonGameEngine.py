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
    glutInitWindowSize(1200,1200)
    glutInitWindowPosition(50,50)
    glutCreateWindow(b'test')
    glutDisplayFunc(plotpoints)
    init()
    
    glutKeyboardFunc(keyboard)
    
    # Add this line to handle mouse movement
    glutMotionFunc(mouseDrag)
    
    glutMainLoop()
    print("Ending...")
    
def mouseDrag(x, y):
    # Update the camera position in real-time
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