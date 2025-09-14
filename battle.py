from util.multichoiceinput import get_multichoice_input
import random


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

        self.start_battle()
        self.end_battle()

    def start_battle(self):
        # return immediately if player or enemy doesn't exist
        if not (self.player and self.enemy):
            print("Can't start battle, one or more entities unresolved.")
            return

        # battle loop
        while self.player.health > 0 and self.enemy.health > 0:
            print(f"\n{self.player.name} HP: {self.player.health} | {self.enemy.name} HP: {self.enemy.health}")

            self.__player_turn()
            self.__enemy_turn()

            if self.enemy.health <= 0:
                print(f"\n{self.enemy.name} has been defeated!")

            if self.player.health <= 0:
                print(f"\n{self.player.name} has been defeated!")

    def end_battle(self):
        self.player = None
        self.enemy = None

    def __player_turn(self):
        print("Choose your move:")
        choice = get_multichoice_input([
            "Attack",
            "Defend",
            "Flee"
        ])
        match choice:
            case 1:
                print(f"You attack enemy for {self.player.get_damage()} damage.")
                self.enemy.take_damage(self.player.get_damage())
            case 2:
                print("Defended")
                self.player.blocking = True
            case 3:
                print("Fled")

    def __enemy_turn(self):
        choice = random.choice([1, 2])

        match choice:
            case 1:
                print(f"{self.enemy.name} attacks!")
                self.player.take_damage(self.enemy.get_damage())
            case 2:
                print(f"{self.enemy.name} defends!")
                self.enemy.blocking = True
