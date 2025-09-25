from util.multichoiceinput import get_multichoice_input
from factory import enemyfactory
from battle import Battle
import random
from factory.eventfactory import create_path_scenario, get_random_enemy_type, create_building_scenario


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
    scenario = create_building_scenario()

    print(scenario["description"])
    choice = get_multichoice_input(scenario["choices"])
    chosen_path = scenario["choices"][choice - 1]

    if choice == 1:
        print(f"You {chosen_path}.")
        outcome = random.choice(["treasure", "enemy"])

        if outcome == "treasure":
            treasure_event(player)
        else:
            enemy_event(player, "random")

    else:
        print(f"You {chosen_path}")



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

def treasure_event(player):
    treasures = [
        {"description": "You find a dusty chest containing gold coins!", "effect": "heal", "amount": 5},
        {"description": "An old potion sits on a shelf, still glowing faintly.", "effect": "heal", "amount": 3},
        {"description": "You discover a hidden stash of supplies!", "effect": "heal", "amount": 4},
        {"description": "A mysterious herb grows in the corner.", "effect": "heal", "amount": 2},
        {"description": "You find an abandoned weapon rack with a usable weapon!", "effect": "weapon", "amount": 0}
    ]

    treasure = random.choice(treasures)
    print(treasure["description"])

    if treasure["effect"] == "heal":
        player.heal(treasure["amount"])
        player.gain_xp(2)
    elif treasure["effect"] == "weapon":
        from factory.weaponfactory import create_random_weapon
        weapon = create_random_weapon()
        print(f"You found: {weapon}")

        choice = get_multichoice_input([
            f"Equip the {weapon.name}",
            "Leave it behind"
        ])

        if choice == 1:
            player.equip_weapon(weapon)

        player.gain_xp(3)



def random_event(player):
    events = [enemy_event, safe_event, building_event]
    event = random.choice(events)

    if event == enemy_event:
        event(player, "random")
    else:
        event(player)
