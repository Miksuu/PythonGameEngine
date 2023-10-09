from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from GameObject import GameObject

from GameObjectManager import GameObjectManager

gameObjectManager = GameObjectManager

class WindowManagement:
    def __init__(self, gameObjectManager, windowSizeX, windowSizeY):
        # Setup the GameObjectManager ref
        self.gameObjectManager = gameObjectManager
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY
        
    def setupWindow(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(self.windowSizeX, self.windowSizeY)
        glutCreateWindow("test")
        #glutIdleFunc(self.idleFunctionWrapper)
        glutDisplayFunc(self.plotpoints)
        glClearColor(0.0,0.0,0.0,1.0)
        gluOrtho2D(-1.0,1.0,-1.0,1.0)
    
    def plotpoints(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.gameObjectManager.handleGameLoop()
        glutSwapBuffers()
        glFlush()
        
    def idleFunctionWrapper(self):
        self.gameObjectManager.handleGameLoop()
       # glutPostRedisplay()
