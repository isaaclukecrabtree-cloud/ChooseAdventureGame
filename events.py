import tkinter as tk
from enemy import Enemy


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


def building_event(player):
    print("A seemingly abandoned building can be seen in the distance, do you wish to explore it?")


def random_event(player):
    events = [enemy_event, safe_event, treasure_event, building_event]
    event = treasure_event
    # event = random.choice(events)
    event(player, events)
