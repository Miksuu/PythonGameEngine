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

# Create a green wall as another game object
# wall = GameObject(-1.0, -1.0, (0.0, 1.0, 0.0), None)  # point_size is not used for wall

# wallPoints = []
# for i in range(-10, 11):  # This creates 21 points
#     x = i * 0.1
#     y = -0.9  # Y-coordinate is fixed for the wall points
#     point = GameObject(x, y, (0.0, 1.0, 0.0), 5.0)
#     wallPoints.append(point)

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    gameObjectManager.handleGameLoop()
    #renderMultiplePoints(wallPoints)  # Render the wall points
    glFlush()

    
# def renderWall():
#     # Render the wall
#     glColor3f(0.0, 1.0, 0.0)  # Set color to green
#     glBegin(GL_QUADS)  # Start drawing a quad
#     glVertex2f(wall_x1, wall_y1)  # Bottom-left corner
#     glVertex2f(wall_x2, wall_y1)  # Bottom-right corner
#     glVertex2f(wall_x2, wall_y2)  # Top-right corner
#     glVertex2f(wall_x1, wall_y2)  # Top-left corner
#     glEnd()  # End drawing
    

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


# def check_collision():
#     global object_x, object_y
#     if wall_x1 < object_x < wall_x2 and wall_y1 < object_y < wall_y2:
#         return True
#     return False


def keyboard(key, x, y):
    inputManager.move(key)

main()