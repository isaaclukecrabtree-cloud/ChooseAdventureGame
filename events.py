import tkinter as tk
from factory import enemyfactory
from battle import Battle
import random
from util.multichoiceinput import get_multichoice_input

def enemy_event(player, enemy_type="Goblin"):
    enemy_types = ["Goblin", "Ogre", "Josh", "Demon"]

    if enemy_type == "random":
        enemy_type = random.choice(enemy_types)

    print(f"A {enemy_type} appears!")

    if enemy_type == "Goblin":
        enemy = enemyfactory.create_goblin()
    elif enemy_type == "Ogre":
        enemy = enemyfactory.create_ogre()
    elif enemy_type == "Josh":
        enemy = enemyfactory.create_josh()
    elif enemy_type == "Demon":
        enemy = enemyfactory.create_demon()
    else:
        print(f"Unknown enemy type: {enemy_type}, defaulting to Goblin")
        enemy = enemyfactory.create_goblin()

    Battle(player, enemy)

def safe_event(player):
    print("You find a clear and calm area to rest")
    print(f"You awake feeling refreshed.")
    player.heal(3)


def building_event(player):
    print("A seemingly abandoned building can be seen in the distance, do you wish to explore it?")


def path_event(player):
    scenarios = [
        {
            "description": "The path splits into two directions.",
            "choices": ["Go left", "Go right"]
        },
        {
            "description": "You see a mysterious glow in the distance.",
            "choices": ["Continue on the path", "Go towards the glow"]
        },
        {
            "description": "The road forks at a weathered signpost.",
            "choices": ["Take the mountain path", "Take the forest path"]
        },
        {
            "description": "You hear strange sounds echoing from different directions.",
            "choices": ["Follow the loud sounds", "Head away from the noises"]
        },
        {
            "description": "Two bridges cross a rushing river ahead.",
            "choices": ["Take the stone bridge", "Take the wooden bridge"]
        }
    ]

    scenario = random.choice(scenarios)

    print(scenario["description"])
    choice = get_multichoice_input(scenario["choices"])

    chosen_path = scenario["choices"][choice - 1]
    print(f"You chose: {chosen_path}")
    print("You continue on your journey...")

    other_events = [enemy_event, safe_event, building_event]
    next_event = random.choice(other_events)

    if next_event == enemy_event:
        next_event(player, "random")
    else:
        next_event(player)

def random_event(player):
    events = [enemy_event, safe_event, building_event]
    event = random.choice(events)

    if event == enemy_event:
        event(player, "random")
    else:
        event(player)
