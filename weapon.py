import random
from enum import Enum


class Colour(Enum):
    RESET = "\033[0m"
    RED = "\033[1;31m"
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    YELLOW = "\033[93m"


class Rarity(Enum):
    BROKEN = "Broken", -1, Colour.RED
    COMMON = "Common", 0, Colour.WHITE
    UNCOMMON = "Uncommon", 1, Colour.GREEN
    RARE = "Rare", 2, Colour.BLUE
    EPIC = "Epic", 3, Colour.PURPLE
    LEGENDARY = "Legendary", 5, Colour.YELLOW

    def __init__(self, display_name, damage_bonus, colour):
        self.display_name = display_name
        self.damage_bonus = damage_bonus
        self.colour = colour


class WeaponType(Enum):
    DAGGER = "Dagger", 2
    AXE = "Axe", 3
    SWORD = "Sword", 4
    CLUB = "Club", 2
    SPEAR = "Spear", 4
    GREATSWORD = "Greatsword", 6
    KATANA = "Katana", 5
    SHOVEL = "Shovel", 3

    def __init__(self, display_name, base_damage):
        self.display_name = display_name
        self.base_damage = base_damage


class Weapon:
    def __init__(self, weapon_type: WeaponType, rarity: Rarity):
        self.weapon_type = weapon_type
        self.rarity = rarity

    @property
    def name(self) -> str:
        return self.weapon_type.display_name

    @property
    def total_damage(self) -> int:
        return self.weapon_type.base_damage + self.rarity.damage_bonus

    @property
    def colour(self) -> str:
        return self.rarity.colour.value

    def __str__(self) -> str:
        return f"{self.colour}{self.rarity.display_name} {self.name}{Colour.RESET.value} (+{self.total_damage} damage.)"


def create_random_weapon() -> Weapon:
    weapon_type = random.choice(list(WeaponType))
    rarity = random.choice(list(Rarity))
    return Weapon(weapon_type, rarity)


def create_weapon(weapon_type: WeaponType, rarity: Rarity) -> Weapon:
    return Weapon(weapon_type, rarity)
