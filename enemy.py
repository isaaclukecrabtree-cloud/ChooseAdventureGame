from lifeform import Lifeform

class Enemy(Lifeform):
    def stats(self):
        return f"Enemy: {self.name}\nHealth: {self.health}\nDamage: {self.base_damage}\n"
