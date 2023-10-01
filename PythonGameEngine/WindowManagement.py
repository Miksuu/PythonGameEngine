from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from GameObject import GameObject

from GameObjectManager import GameObjectManager

gameObjectManager = GameObjectManager

class WindowManagement:
    windowSizeX = 1337
    windowSizeY = 1337
    def __init__(self, gameObjectManager, _windowSizeX, _windowSizeY):
        # Setup the GameObjectManager ref
        self.gameObjectManager = gameObjectManager
        windowSizeX = _windowSizeX
        windowSizeY = _windowSizeY
    
    def setupWindow(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(self.windowSizeX,self.windowSizeY)
        glutInitWindowPosition(50,50)
        glutCreateWindow(b'test')
        glutDisplayFunc(self.plotpoints)
        glClearColor(0.0,0.0,0.0,1.0)
        gluOrtho2D(-1.0,1.0,-1.0,1.0)
    
    def plotpoints(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.gameObjectManager.handleGameLoop()
        glutSwapBuffers()
        glFlush()