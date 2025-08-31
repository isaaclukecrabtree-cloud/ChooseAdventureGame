class Enemy:

    def __init__(self, name="Goblin", health=5, damage=2):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, player):
        player.take_damage(self.damage)()
        print (f"{self.name} attacks {player.name} for {self.damage} damage!")

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)


    def stats(self):
        return (f"Enemy: {self.name}\n"
                f"Health: {self.health}\n"
                f"Damage: {self.damage}\n")
