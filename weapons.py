import random

class Colours:
    reset = "\033[0m"
    red = "\033[1;31m"
    white = "\033[97m"
    green = "\033[92m"
    blue = "\033[94m"
    purple = "\033[95m"
    yellow = "\033[93m"

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


rarities = {
    "Broken":    (-1, Colours.red),
    "Common":    (0, Colours.white),
    "Uncommon":  (1, Colours.green),
    "Rare":      (2, Colours.blue),
    "Epic":      (3, Colours.purple),
    "Legendary": (5, Colours.yellow),
}

weapons = [
    ("Dagger", 2),
    ("Axe", 3),
    ("Sword", 4),
    ("Club", 2),
    ("Spear", 4),
    ("Greatsword", 6),
    ("Katana", 5),
    ("Shovel", 3),
]

def random_weapon():
    weapon_name, base_damage = random.choice(weapons)
    rarity, (bonus, colour) = random.choice(list(rarities.items()))
    total_damage = base_damage + bonus
    return Weapon(weapon_name, rarity, total_damage, colour)

def format_weapon(weapon:Weapon):
    return f"{weapon.colour}{weapon.rarity} {weapon.name}{Colours.reset} (+{weapon.damage} damage.)"