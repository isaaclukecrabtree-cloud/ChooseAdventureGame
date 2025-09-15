import random
from weapon import WeaponType, Rarity, Weapon

#random weapon and rarity
def create_random_weapon() -> Weapon:
    weapon_type = random.choice(list(WeaponType))
    rarity = random.choice(list(Rarity))
    return Weapon(weapon_type, rarity)

#specific weapon and rarity
def create_weapon(weapon_type: WeaponType, rarity: Rarity) -> Weapon:
    return Weapon(weapon_type, rarity)

