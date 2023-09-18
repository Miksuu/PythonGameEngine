from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys


class GameObject:
    def __init__(self, x, y, color, point_size):
        self.x = x
        self.y = y
        self.color = color
        self.point_size = point_size

    def render(self):
        glColor3f(*self.color)
        glPointSize(self.point_size)
        glBegin(GL_POINTS)
        glVertex2f(self.x, self.y)
        glEnd()

class GameObjectManager:
    def __init__(self):
        self.worldObjects = []
        
    def addObject(self, gameObjectToAdd):
        self.worldObjects.append(gameObjectToAdd)
    
gameObjectManager = GameObjectManager()
# Create a red point as a game object
player = GameObject(0.0, 0.0, (1.0, 0.0, 0.0), 10.0)

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
    player.render()  # Render the player
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
    

def renderMultiplePoints(game_objects):
    for obj in game_objects:
        obj.render()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow(b'test')
    glutDisplayFunc(plotpoints)
    init()
    
    glutKeyboardFunc(keyboard)

    glutMainLoop()


# def check_collision():
#     global object_x, object_y
#     if wall_x1 < object_x < wall_x2 and wall_y1 < object_y < wall_y2:
#         return True
#     return False


def keyboard(key, x, y):
    global player, prev_object_x, prev_object_y

    # Store the object's current position before moving
    # prev_object_x, prev_object_y = object_x, object_y
    
    if ord(key) == ord('w'):  # Move Up
        player.y += 0.1
    elif ord(key) == ord('s'):  # Move Down
        player.y -= 0.1
    elif ord(key) == ord('a'):  # Move Left
        player.x -= 0.1
    elif ord(key) == ord('d'):  # Move Right
        player.x += 0.1
        
    # if check_collision():
    #     print("Collision detected!")
    #     # Revert movement
    #     object_x, object_y = prev_object_x, prev_object_y

    if ord(key) == 27:  # ESC key
        print("Exiting...")
        glutLeaveMainLoop()
    glutPostRedisplay()

main()