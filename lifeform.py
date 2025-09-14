from weapon import Weapon, WeaponType


class Lifeform:
    def __init__(self, name, health, base_damage):
        self.name = name
        self.health = health
        self.max_health = health
        self.base_damage = base_damage
        self.equipped_weapon = None  # Add this line

        self.blocking = False

    def take_damage(self, damage):
        damage_taken = damage
        if self.blocking:
            damage_taken /= 2
        self.health -= damage_taken
        self.blocking = False

    def get_damage(self):
        base_damage = self.base_damage
        weapon_damage = 0

        if self.equipped_weapon:
            weapon_damage = self.equipped_weapon.damage

        return base_damage + weapon_damage

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} healed for {amount}. Health is now: {self.health}/{self.max_health}.")
