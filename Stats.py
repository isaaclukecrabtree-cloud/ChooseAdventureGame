class Player:

    def __init__(self, name, health=10, damage=1, charisma=1, stealth=0):
        self.name = name
        self.max_health = health
        self.health = health
        self.base_damage = damage
        self.charisma = charisma
        self.stealth = stealth
        self.weapon = None

    def damage(self):
        return self.base_damage + (self.weapon[1] if self.weapon else 0)

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print (f"{self.name} equips the {weapon[0]} (+{weapon[1]} damage).")

    def attack(self, enemy):
        enemy.take_damage(self.damage)()
        print (f"{self.name} attacks {enemy.name} for {self.damage} damage!.")
        if enemy.health <= 0:
            print (f"{enemy.name} has been defeated!")

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print (f"{self.name} healed for {amount}. Health is now: {self.health}/{self.max_health}.")

    def is_alive(self):
        return self.health > 0

    def stats(self):
        return (f"Player: {self.name}\n"
                f"Health: {self.health}\n"
                f"Damage: {self.damage}\n"
                f"Charisma: {self.charisma}\n")
