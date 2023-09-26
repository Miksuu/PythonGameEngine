from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

# Engine components
from Camera import Camera
from GameObject import GameObject
from TriangleGameObject import TriangleGameObject
from GameObjectManager import GameObjectManager
from Vector2 import Vector2

gameObjectManager = GameObjectManager()

camera = Camera()

# x, y positions as Vector2, color, pointSize, speed, camera ref
player = GameObject(Vector2(0.1, 0.2), (1.0, 0.5, 0.0), 10.0, 0.1, camera)

gameObjectManager.addObject(player)

draggingMouse = False

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
    
    # Lines to handle mouse movement
    glutMouseFunc(mouseButton)
    glutMotionFunc(mouseDrag)
    
    glutMainLoop()
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
            # x, y positions as Vector2, color, pointSize, speed, camera ref, velocity
            projectile_velocity = Vector2(0.05, 0.05)  # Add a velocity vector for the projectile
            projectile = TriangleGameObject(Vector2(player.position.x, player.position.y), (0.2, 1.0, 0.2), 10.0, 0.1, projectile_velocity)
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