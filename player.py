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
        print (f"{self.name} equips the {weapon[0]} (+{weapon[1]} damage).")

    def get_damage(self):
        return self.base_damage + (self.weapon[1] if self.weapon else 0)

    def stats(self):
        return (f"Player: {self.name}\n"
                f"Health: {self.health}\n"
                f"Damage: {self.get_damage()}\n"
                f"Charisma: {self.charisma}\n")

    def set_class_assassin(self):
        self.base_damage = 2
        self.charisma = 1
        self.stealth = 4
        self.max_health = 6
        self.health = self.max_health
    
    def set_class_warrior(self):
        self.base_damage = 3
        self.charisma = 1
        self.stealth = 1
        self.max_health = 9
        self.health = self.max_health
    
    def set_class_tank(self):
        self.base_damage = 1
        self.charisma = 1
        self.stealth = 0
        self.max_health = 13
        self.health = self.max_health



