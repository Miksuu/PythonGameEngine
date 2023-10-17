import time
from Character import Character
from Gun import Gun
from Vector2 import Vector2
from Renderer import Renderer

class AI(Character):
    def __init__(self, name, transform):
        super().__init__(name, transform)
        self.equippedGun = Gun("Pistol", 10)
        
        self.lastShootTime = 0
        self.shootInterval = 2
        
        self.renderer = Renderer(None, name, transform)
        
    def update(self):
        super().update()
        
    def automaticShooting(self, gameObjectManager, aiList):
        currentTime = time.time()
        if currentTime - self.lastShootTime >= self.shootInterval:
            closest_ai = self.findClosestTarget(self.transform.position, aiList)
            if closest_ai:
                targetPosition = closest_ai.transform.position
                self.attack(Vector2(targetPosition.x, targetPosition.y), gameObjectManager)
                self.lastShootTime = currentTime
            else:
                print("No target found.")
            
    def findClosestTarget(self, fromPosition, aiList):
        closestAi = None
        closestDistance = float('inf')

        for ai in aiList:
            if ai.transform.position == fromPosition:
                continue

            distance = (fromPosition - ai.transform.position).magnitude()
            if distance < closestDistance:
                closestDistance = distance
                closestAi = ai

        return closestAi