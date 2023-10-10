import time
from Character import Character
from Gun import Gun
from Vector2 import Vector2
from Renderer import Renderer

class AI(Character):
    def __init__(self, name, transform):
        super().__init__(name, transform)
        self.equipped_gun = Gun("Pistol", 10)
        
        self.lastShootTime = 0
        self.shootInterval = 2
        
        self.renderer = Renderer(None, name, transform)
        
    def update(self):
        super().update()
        
    def automaticShooting(self, gameObjectManager, aiList):
        currentTime = time.time()
        if currentTime - self.lastShootTime >= self.shootInterval:
            closest_ai = self.FindClosestTarget(self.transform.position, aiList)
            if closest_ai:
                target_position = closest_ai.transform.position
                self.attack(target_position.x, target_position.y, gameObjectManager)
                self.lastShootTime = currentTime
            else:
                print("No target found.")
            
    def FindClosestTarget(self, fromPosition, aiList):
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