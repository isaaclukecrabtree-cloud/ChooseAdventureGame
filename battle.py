from util.multichoiceinput import get_multichoice_input
import random
import time


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.fled = False

        self.start_battle()
        self.end_battle()

    def start_battle(self):
        # return immediately if player or enemy doesn't exist
        if not (self.player and self.enemy):
            print("Can't start battle, one or more entities unresolved.")
            return

        # battle loop
        while self.player.health > 0 and self.enemy.health > 0 and not self.fled:
            player_name_len = len(self.player.name)
            enemy_name_len = len(self.enemy.name)

            print(f"\n{self.player.name} HP: {self.player.health} | {self.enemy.name} HP: {self.enemy.health}")
            print(f"{' ' * player_name_len}Dmg: {self.player.get_damage()} | {' ' * enemy_name_len}Dmg: {self.enemy.get_damage()}")

            self.__player_turn()
            self.__enemy_turn()

        # Battle end messages
        if self.fled:
            print(f"\n{self.player.name} escaped from battle!")
        elif self.enemy.health <= 0:
            print(f"\n{self.enemy.name} has been defeated!")
        elif self.player.health <= 0:
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
                time.sleep(0.5)
            case 2:
                print("Defended")
                self.player.blocking = True
                time.sleep(0.5)
            case 3:
                if random.random() < 0.5:
                    print("You successfully fled from combat!")
                    self.fled = True
                    time.sleep(0.5)
                else:
                    print("You tried to flee but couldn't escape!")
                    time.sleep(0.5)

    def __enemy_turn(self):
        if self.enemy.health <= 0 or self.fled:  # Combined check
            return

        choice = random.choice([1, 2])

        match choice:
            case 1:
                print(f"{self.enemy.name} attacks for {self.enemy.get_damage()} damage.!")
                self.player.take_damage(self.enemy.get_damage())
                time.sleep(0.5)
            case 2:
                print(f"{self.enemy.name} defends!")
                self.enemy.blocking = True
                time.sleep(0.5)
