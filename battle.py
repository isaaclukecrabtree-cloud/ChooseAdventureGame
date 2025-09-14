from util import *
from util.multichoiceinput import get_multichoice_input

class Battle:
    @staticmethod
    def start_battle(player, enemy):
        Battle.player_turn(player)
    @staticmethod
    def player_turn(player):
        choice = get_multichoice_input([
            "Attack",
            "Defend",
            "Flee"
        ])

        if choice == "1":
            print("Attacked")
        elif choice == "2":
            print("Defended")
        elif choice == "3":
            print("Fleed")
