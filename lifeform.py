class Lifeform:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} healed for {amount}. Health is now: {self.health}/{self.max_health}.")
