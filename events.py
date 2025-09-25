from util.multichoiceinput import get_multichoice_input
from factory import enemyfactory
from battle import Battle
import random
from factory.eventfactory import create_path_scenario, get_random_enemy_type


def enemy_event(player, enemy_type="Goblin"):
    if enemy_type == "random":
        enemy_type = get_random_enemy_type()

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

    enemy.scale_to_player_level(player.level)

    Battle(player, enemy)


def safe_event(player):
    print("You find a clear and calm area to rest")
    print(f"You awake feeling refreshed.")
    player.heal(3)


def building_event(player):
    print("A seemingly abandoned building can be seen in the distance, do you wish to explore it?")


def path_event(player):
    scenario = create_path_scenario()

    print(scenario["description"])
    choice = get_multichoice_input(scenario["choices"])
    chosen_path = scenario["choices"][choice - 1]
    print(f"You {chosen_path}")

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
