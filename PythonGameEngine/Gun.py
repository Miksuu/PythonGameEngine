from Transform import Transform
from Vector2 import Vector2
from Bullet import Bullet

class Gun:
    def __init__(self, weapon_name, damage):
        self.weapon_name = weapon_name
        self.damage = damage

    def shoot(self, characterTransform, x, y, gameObjectManager):
        projectileTransform = Transform(Vector2(characterTransform.position.x, characterTransform.position.y))
        projectile = Bullet("Bullet", projectileTransform, x, y)
        projectile.velocity = Vector2(1, 1)  # Temp Setting the projectile to go with 1,1 velocity
        gameObjectManager.addObject(projectile)
