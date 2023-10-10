from Vector2 import Vector2
from Bullet import Bullet

class Gun:
    def __init__(self, weapon_name, damage):
        self.weapon_name = weapon_name
        self.damage = damage

    def shoot(self, character_position, x, y, gameObjectManager):
        projectilePosition = Vector2(character_position.x, character_position.y)
        projectile = Bullet("Bullet", projectilePosition, x, y)
        projectile.velocity = Vector2(1, 1)  # Temp Setting the projectile to go with 1,1 velocity
        gameObjectManager.addObject(projectile)
