class GameObjectManager:
    def __init__(self):
        self.worldObjects = []
        
    def addObject(self, gameObjectToAdd):
        self.worldObjects.append(gameObjectToAdd)
        
    def handleGameLoop(self):
        for obj in self.worldObjects:
            obj.handleGameLoop()