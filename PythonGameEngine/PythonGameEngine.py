from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

object_x = 0.0
object_y = 0.0

wall_x1, wall_y1 = -1.0, -1.0  # Bottom-left corner
wall_x2, wall_y2 = 1.0, -0.9  # Top-right corner

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def plotpoints():
    global object_x, object_y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    
    glVertex2f(object_x,object_y)
    glEnd()    

    renderWallTest()


    glFlush()
    
def renderWallTest():
    # Render the wall
    glColor3f(0.0, 1.0, 0.0)  # Set color to green
    glBegin(GL_QUADS)  # Start drawing a quad
    glVertex2f(wall_x1, wall_y1)  # Bottom-left corner
    glVertex2f(wall_x2, wall_y1)  # Bottom-right corner
    glVertex2f(wall_x2, wall_y2)  # Top-right corner
    glVertex2f(wall_x1, wall_y2)  # Top-left corner
    glEnd()  # End drawing
    

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


def check_collision():
    global object_x, object_y
    if wall_x1 < object_x < wall_x2 and wall_y1 < object_y < wall_y2:
        return True
    return False


def keyboard(key, x, y):
    global object_x, object_y, prev_object_x, prev_object_y

    # Store the object's current position before moving
    prev_object_x, prev_object_y = object_x, object_y
    
    if ord(key) == ord('w'):  # Move Up
        object_y += 0.1
    elif ord(key) == ord('s'):  # Move Down
        object_y -= 0.1
    elif ord(key) == ord('a'):  # Move Left
        object_x -= 0.1
    elif ord(key) == ord('d'):  # Move Right
        object_x += 0.1
        
    if check_collision():
        print("Collision detected!")
        # Revert movement
        object_x, object_y = prev_object_x, prev_object_y

    if ord(key) == 27:  # ESC key
        print("Exiting...")
        glutLeaveMainLoop()
    glutPostRedisplay()

main()