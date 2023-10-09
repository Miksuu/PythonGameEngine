from ast import unaryop
from tkinter import SE
from Renderer import Renderer
from Vector2 import Vector2
from Camera import Camera

# Game class definitions
from InputManager import InputManager

class GameObject:
    def __init__(self, name, position):
        self.name = name
        self.position = Vector2(position.x, position.y)
        self.velocity = Vector2(0, 0)            

    def update(self):
        self.position += self.velocity

    def handleGameLoop(self):
        self.update()
        self.renderer.shader.setShaderUniforms()        
        self.renderer.updateVertexData(self.position)
        self.renderer.drawAsset() 
        
        # Draw coordinates on top of the object, formatted to 2 decimal places
        # infoText = f"{self.name}({self.position.x:.2f}, {self.position.y:.2f})"
        # self.renderer.setTextColor()  # Set text color to white
        # self.renderer.drawText(self.name, self.position, infoText)
        # self.renderer.resetColor()  # Reset to original color
