from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from AI import AI
from AIManager import AIManager
import time

# Engine components
from Camera import Camera
from GameObjectManager import GameObjectManager
from Transform import Transform
from Vector2 import Vector2
from WindowManagement import WindowManagement
from FileManager import FileManager
# GameObjects
from GameObject import GameObject
from Player import Player
from Bullet import Bullet

gameObjectManager = GameObjectManager()
windowManagement = WindowManagement(gameObjectManager, 1200, 1200)

aiManager = AIManager()

draggingMouse = False

lastSpawnTime = 0
spawnInterval = 1

def main():
    print("Starting...")
    global player    

    windowManagement.setupWindow()
    
    glutKeyboardFunc(keyboardDown)
    glutKeyboardUpFunc(keyboardUp)
    glutIdleFunc(idle)
    
    glutMouseFunc(mouseButton)
    glutMotionFunc(mouseDrag)

    player = Player("PlayerCharacter", Transform())
    gameObjectManager.addObject(player)

    glutMainLoop()
    print("Ending...")

def mouseButton(button, state, x, y):
    global draggingMouse

    # if state == GLUT_DOWN:
        #if button == GLUT_RIGHT_BUTTON:
            #draggingMouse = True
            #recenterCamera()

        # if button == GLUT_LEFT_BUTTON:
        #     projectileTransform = Transform(Vector2(player.transform.position.x, player.transform.position.y))
        #     projectile = Bullet("Bullet", projectileTransform, x, y)
        #     gameObjectManager.addObject(projectile)
    #else:
        #draggingMouse = False

def mouseDrag(x, y):
    if draggingMouse:
        player.inputManager.handleMouseMovement(x, y)

def recenterCamera():
    camera.position = player.position

def keyboardDown(key, x, y):
    player.inputManager.keyDown(key)

def keyboardUp(key, x, y):
    player.inputManager.keyUp(key)

def idle():
    player.inputManager.update()
    
    global lastSpawnTime
    currentTime = time.time()
    
    if currentTime - lastSpawnTime >= spawnInterval:
        aiManager.spawnAi(gameObjectManager)
        lastSpawnTime = currentTime
        
    aiManager.handleAIShooting(gameObjectManager)
    
    glutPostRedisplay()

main()