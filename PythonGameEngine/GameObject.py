from Renderer import Renderer

class GameObject:
    def __init__(self, x, y, color, pointSize, speed):
        self.x = x
        self.y = y
        self.color = color
        self.pointSize = pointSize
        self.speed = speed        

        self.renderer = Renderer(color, pointSize)
        
    def handleGameLoop(self):
        self.renderer.render(self.x, self.y)
        