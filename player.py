from lifeform import Lifeform

class Player(Lifeform):
    def __init__(self, name, health=10, damage=1, charisma=1, stealth=0):
        super().__init__(name, health, damage)
        self.max_health = health
        self.base_damage = damage
        self.charisma = charisma
        self.stealth = stealth
        self.weapon = None

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equips the {weapon[0]} (+{weapon[1]} damage).")

    def get_damage(self):
        return self.base_damage + (self.weapon[1] if self.weapon else 0)

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} healed for {amount}. Health is now: {self.health}/{self.max_health}.")

    def stats(self):
        return (f"Player: {self.name}\n"
                f"Health: {self.health}\n"
                f"Damage: {self.get_damage()}\n"
                f"Charisma: {self.charisma}\n")