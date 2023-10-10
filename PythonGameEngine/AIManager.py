import random
import time

from Vector2 import Vector2
from AI import AI

class AIManager:
    def __init__(self):
        self.aiList = []
        
    def spawnAi(self, gameObjectManager):
        #while True:
        x = random.uniform(-1, 1)  # Random x-coordinate near 0
        y = random.uniform(-1, 1)  # Random y-coordinate near 0
        print("Spawning at: ", x, "|", y)
        aiInstance = AI("Soldier", Vector2(x, y))
        self.aiList.append(aiInstance)
        gameObjectManager.addObject(aiInstance)
        #time.sleep(0.1)  # Spawns an AI every X seconds