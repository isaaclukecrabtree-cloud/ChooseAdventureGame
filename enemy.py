from lifeform import Lifeform


class Enemy(Lifeform):
    def __init__(self, name="Unnamed Enemy", health=5, base_damage=1):
        super().__init__(name=name, health=health, base_damage=base_damage)

    def stats(self):
        return (f"Enemy: {self.name}\n"
                f"Health: {self.health}\n"
                f"Damage: {self.base_damage}\n")
