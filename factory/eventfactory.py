import random
from util.multichoiceinput import get_multichoice_input


def create_path_scenario():
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
    return random.choice(scenarios)


def get_random_enemy_type():
    enemy_types = ["Goblin", "Ogre", "Josh", "Demon"]
    return random.choice(enemy_types)


def get_random_event_type():
    event_types = ["enemy", "safe", "building"]
    return random.choice(event_types)
