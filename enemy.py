from lifeform import Lifeform

class Enemy(Lifeform):
    def __init__(self, name="Goblin", health=5, damage=2):
        super().__init__(name, health, damage)

    def attack(self, player):
        player.take_damage(self.damage)
        print(f"{self.name} attacks {player.name} for {self.damage} damage!")

    def stats(self):
        return (f"Enemy: {self.name}\n"
                f"Health: {self.health}\n"
                f"Damage: {self.damage}\n")
