import weapon
from weapon import Weapon


def create_dagger():
    return Weapon(
        name="Dagger",
        damage=2
    )

def create_sword():
    return Weapon(
        name="Sword",
        damage=4
    )

def create_greatsword():
    return Weapon(
        name="Greatsword",
        damage=6
    )

def create_axe():
    return Weapon(
        name="Axe",
        damage=3
    )