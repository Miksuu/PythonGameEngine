from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from AI import AI
from AIManager import AIManager
import time

# Engine components
from Camera import Camera
from GameObjectManager import GameObjectManager
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
spawnInterval = 0.01

def main():
    print("Starting...")
    global player    

    windowManagement.setupWindow()
    
    glutKeyboardFunc(keyboardDown)
    glutKeyboardUpFunc(keyboardUp)
    glutIdleFunc(idle)
    
    glutMouseFunc(mouseButton)
    glutMotionFunc(mouseDrag)

    player = Player("PlayerCharacter", Vector2(0, 0))
    gameObjectManager.addObject(player)

    glutMainLoop()
    print("Ending...")

def mouseButton(button, state, x, y):
    global draggingMouse

    if state == GLUT_DOWN:
        #if button == GLUT_RIGHT_BUTTON:
            #draggingMouse = True
            #recenterCamera()

        if button == GLUT_LEFT_BUTTON:
            projectilePosition = Vector2(player.position.x, player.position.y)
            projectile = Bullet("Bullet", projectilePosition, x, y)
            gameObjectManager.addObject(projectile)
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
    
    # Check if it's time to spawn a new AI
    if currentTime - lastSpawnTime >= spawnInterval:
        aiManager.spawnAi(gameObjectManager)
        lastSpawnTime = currentTime
    
    glutPostRedisplay()

main()
