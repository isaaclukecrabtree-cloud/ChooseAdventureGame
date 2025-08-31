import random
from foes import Enemy
#class Event:
def enemy_event(player):
    print("An enemy appears, prepare to fight!")
    enemy = Enemy("Goblin", health=5, damage=2)

    while player.is_alive() and enemy.is_alive():
        player.attack(enemy)
        if enemy.is_alive():
            enemy.attack(player)
    if player.is_alive():
        print(f"You defeated {enemy.name}!")
        print(player.stats())
    else:
        print("Game Over")

def safe_event(player):
    print("You find a clear and calm area to rest")
    print(f"You awake feeling refreshed.")
    player.heal(3)

def treasure_event(player):
    weapons = [
        ("Dagger", 2),
        ("Axe", 3),
        ("Sword", 4),
        ("Club", 2),
        ("Spear", 4),
        ("Greatsword", 6),
    ]
    weapon = random.choice(weapons)
    print(f"You found a treasure chest! You open it up to find a {weapon[0]}!")
    player.equip_weapon(weapon)

def building_event(player):
    print("A seemingly abandoned building can be seen in the distance, do you wish to explore it?")

def random_event(player):
    events = [enemy_event , safe_event, treasure_event, building_event]
    #event = enemy_event
    event = random.choice(events)
    event(player)

