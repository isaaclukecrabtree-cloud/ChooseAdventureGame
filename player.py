from lifeform import Lifeform

class Player(Lifeform):
    def __init__(self, name):
        self.name = name
        self.character_class = None
        self.health = 0
        self.max_health = 0
        self.base_damage = 0
        self.charisma = 0
        self.stealth = 0

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print (f"{self.name} equips the {weapon.name} (+{weapon.damage} damage).")

    def get_damage(self):
        return self.base_damage + (self.weapon.damage if self.weapon else 0)

    def stats(self):
        return (f"Player: {self.name}\n"
                f"Health: {self.health}\n"
                f"Damage: {self.get_damage()}\n"
                f"Charisma: {self.charisma}\n")

    def set_class_assassin(self):
        self.character_class = "Assassin"
        self.base_damage = 2
        self.charisma = 1
        self.stealth = 4
        self.max_health = 6
        self.health = self.max_health
    
    def set_class_warrior(self):
        self.character_class = "Warrior"
        self.base_damage = 3
        self.charisma = 1
        self.stealth = 1
        self.max_health = 9
        self.health = self.max_health
    
    def set_class_tank(self):
        self.character_class = "Tank"
        self.base_damage = 1
        self.charisma = 1
        self.stealth = 0
        self.max_health = 13
        self.health = self.max_health



