from lifeform import Lifeform

class Player(Lifeform):
    def __init__(self, name, health=10, damage=1, charisma=1, stealth=0):
        super().__init__(name, health, damage)
        self.max_health = health
        self.base_damage = damage
        self.charisma = charisma
        self.stealth = stealth
        self.weapon = None

    def get_damage(self):
        return self.base_damage + (self.weapon[1] if self.weapon else 0)

    def stats(self):
        return (f"Player: {self.name}\n"
                f"Health: {self.health}\n"
                f"Damage: {self.get_damage()}\n"
                f"Charisma: {self.charisma}\n")

def set_class_assassin(player):
    player.base_damage = 2
    player.charisma = 1
    player.stealth = 4
    player.health = 6
    return player

def set_class_warrior(player):
    player.base_damage = 3
    player.charisma = 1
    player.stealth = 1
    player.health = 8
    return player

def set_class_tank(player):
    player.base_damage = 1
    player.charisma = 1
    player.stealth = 0
    player.health = 13
    return player



