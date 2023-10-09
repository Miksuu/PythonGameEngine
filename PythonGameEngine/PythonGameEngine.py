from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

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

projectileCount = 0

draggingMouse = False

def main():
    print("Starting...")
    global player    

    windowManagement.setupWindow()
    
    glutKeyboardFunc(keyboard)
    
    # Lines to handle mouse movement
    glutMouseFunc(mouseButton)
    glutMotionFunc(mouseDrag)

    # name, x, y positions as Vector2, color, speed, camera ref
    player = Player("PlayerCharacter", Vector2(0, 0))
    gameObjectManager.addObject(player)
    
    # Run the GLUT mainloop
    print("Starting GLUT Main Loop")
    glutMainLoop()
    
    print("Ending...")

def mouseButton(button, state, x, y):
    global draggingMouse

    if state == GLUT_DOWN:
        # Dragging mouse, camera control
        if button == GLUT_RIGHT_BUTTON:
            draggingMouse = True
            #recenterCamera() # Re-center when the button is released

        # Shooting mechanics implementation
        if button == GLUT_LEFT_BUTTON:
            global projectileCount
            # x, y positions as Vector2, color, speed, camera ref, velocity
            projectilePosition = Vector2(player.position.x, player.position.y)
            #projectile = Bullet("Bullet" + str(projectileCount), projectilePosition, projectileColor, x, y)
            projectile = Bullet("Bullet", projectilePosition, x, y)
            gameObjectManager.addObject(projectile)
            projectileCount += 1
    else:
        draggingMouse = False

def mouseDrag(x, y):
    if draggingMouse:
        player.inputManager.handleMouseMovement(x, y)
        # Need to keep updating the position while mouse is on the movement
        glutPostRedisplay()

def recenterCamera():
    camera.position = player.position

def keyboard(key, x, y):
    player.inputManager.move(key)

main()
