from util.multichoiceinput import get_multichoice_input
import random


class Battle:
    @staticmethod
    def start_battle(player, enemy):
        while player.health > 0 and enemy.health > 0:
            print(f"\n{player.name} HP: {player.health} | {enemy.name} HP: {enemy.health}")

            Battle.player_turn(player, enemy)
            Battle.enemy_turn(enemy, player)

            if enemy.health <= 0:
                print(f"\n{enemy.name} has been defeated!")

            if player.health <= 0:
                print(f"\n{player.name} has been defeated!")

    @staticmethod
    def player_turn(player, enemy):
        print("Choose your move:")
        choice = get_multichoice_input([
            "Attack",
            "Defend",
            "Flee"
        ])
        match choice:
            case 1:
                print(f"You attack enemy for {player.get_damage()} damage.")
                enemy.take_damage(player.get_damage())
            case 2:
                print("Defended")
                player.blocking = True
            case 3:
                print("Fled")


    @staticmethod
    def enemy_turn(enemy, player):
        enemy_choice = random.choice([1, 2])

        if enemy_choice == 1:
            print(f"{enemy.name} attacks!")
            player.take_damage(enemy.get_damage())
        elif enemy_choice == 2:
            print(f"{enemy.name} defends!")
        enemy.blocking = True