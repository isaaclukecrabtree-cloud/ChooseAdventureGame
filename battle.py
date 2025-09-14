from util import *
from util.multichoiceinput import get_multichoice_input
import random

class Battle:
    @staticmethod
    def start_battle(player, enemy):
        for turn in range(3):
            Battle.player_turn(player)
            Battle.enemy_turn(enemy)

        # while player.health > 0 and enemy.health > 0:
            print(f"\n{player.name} HP: {player.health} | {enemy.name} HP: {enemy.health}")

            if enemy.health <= 0:
                print(f"\n{enemy.name} has been defeated!")

            if player.health <= 0:
                print(f"\n{player.name} has been defeated!")

    @staticmethod
    def player_turn(player):
        choice = get_multichoice_input([
            "Attack",
            "Defend",
            "Flee"
        ])
        print(choice)
        match choice:
            case 1:
                print("Attacked")
            case 2:
                print("Defended")
            case 3:
                print("Fleed")

    @staticmethod
    def enemy_turn(enemy):
        enemy_choice = random.choice([1, 2])

        if enemy_choice == 1:
            print(f"{enemy.name} attacks!")
        elif enemy_choice == 2:
            print(f"{enemy.name} defends!")
