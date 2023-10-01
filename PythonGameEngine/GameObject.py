from tkinter import SE
from turtle import position, update
from Renderer import Renderer
from Vector2 import Vector2

# Game class definitions
from InputManager import InputManager

class GameObject:
    def __init__(self, name, vertices, position, color, speed, camera):
        self.name = name
        self.position = Vector2(position.x, position.y)
        self.color = color
        self.speed = speed

        # Add input to the player only
        if camera is None:
            pass
        else:
            self.inputManager = InputManager(self, camera)

        self.renderer = Renderer(vertices, color, camera)
        self.vertices = vertices
        
    def handleGameLoop(self):
        self.renderer.setShaderUniforms()        

        self.renderer.updateVertexData(self.position)
        self.renderer.drawVboRectangle()

        #print(f"Updated vertices: {self.vertices}")        

        # Draw coordinates on top of the object, formatted to 2 decimal places
        #infoText = f"{self.name}({self.position.x:.2f}, {self.position.y:.2f})"
        #self.renderer.setTextColor((1.0, 1.0, 1.0))  # Set text color to white
        #self.renderer.drawText(self.name, self.position, infoText)
        #self.renderer.resetColor()  # Reset to original color
