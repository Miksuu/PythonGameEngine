from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

object_x = 0.0
object_y = 0.0

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
    glFlush()

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


def keyboard(key, x, y):
    global object_x, object_y
    if ord(key) == ord('w'):  # Move Up
        object_y += 0.01
    elif ord(key) == ord('s'):  # Move Down
        object_y -= 0.01
    elif ord(key) == ord('a'):  # Move Left
        object_x -= 0.01
    elif ord(key) == ord('d'):  # Move Right
        object_x += 0.01
    if ord(key) == 27:  # ESC key
        print("Exiting...")
        glutLeaveMainLoop()

main()