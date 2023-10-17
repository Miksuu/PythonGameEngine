from Transform import Transform
from Vector2 import Vector2
from Bullet import Bullet

class Gun:
    def __init__(self, weapon_name, damage):
        self.weapon_name = weapon_name
        self.damage = damage

    def shoot(self, characterTransform, targetVec2, gameObjectManager):
        projectileTransform = Transform(Vector2(characterTransform.position.x, characterTransform.position.y))
        projectile = Bullet("Bullet", projectileTransform, targetVec2)
        gameObjectManager.addObject(projectile)
