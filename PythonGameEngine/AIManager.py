import random
import time

from Vector2 import Vector2
from AI import AI

class AIManager:
    def __init__(self):
        self.aiList = []

    def spawnAi(self, gameObjectManager):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        print("Spawning at: ", x, "|", y)
        aiInstance = AI("Soldier", Vector2(x, y))
        self.aiList.append(aiInstance)
        gameObjectManager.addObject(aiInstance)
        
    def handleAIShooting(self, gameObjectManager):
        for ai in self.aiList:
            ai.automaticShooting(gameObjectManager)            
