from lifeform import Lifeform
from config import CharacterClass

class Player(Lifeform):
    def __init__(self, name="..."):
        super().__init__(name, 5, 1)
        self.charisma = 0
        self.stealth = 0

        self.character_class = None
        self.equipped_weapon = None

        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 10  # XP needed to reach level 2

    def gain_xp(self, amount):
        print(f"+{amount} XP gained!")
        self.xp += amount

        while self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.xp -= self.xp_to_next_level  # Carry over excess XP
        self.level += 1

        print(f"\nLEVEL UP! You are now level {self.level}!")

        old_health = self.max_health
        old_damage = self.base_damage

        if self.character_class == CharacterClass.WARRIOR:
            self.max_health += 4
            self.base_damage += 2
        elif self.character_class == CharacterClass.ASSASSIN:
            self.max_health += 2
            self.base_damage += 2
            self.stealth += 2
        elif self.character_class == CharacterClass.TANK:
            self.max_health += 5
            self.base_damage += 2

        self.health = self.max_health

        self.xp_to_next_level = self.calculate_xp_for_next_level()

        print(f"Health: {old_health} -> {self.max_health}")
        print(f"Damage: {old_damage} -> {self.base_damage}")
        if self.character_class == CharacterClass.ASSASSIN and self.level > 1:
            print(f"Stealth increased!")

    def calculate_xp_for_next_level(self):
        return self.level * 10

    def set_class(self, character_class):
        self.character_class = character_class
        self.health = self.max_health = character_class.max_health
        self.base_damage = character_class.base_damage
        self.charisma = character_class.charisma
        self.stealth = character_class.stealth

    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon
        print(f"{self.name} picks up the {weapon}")

    def display_stats(self):
        class_name = self.character_class.display_name if self.character_class else "None"
        print(f"""Your character details:
        Name: {self.name}
        Class: {class_name}
        Health: {self.health}/{self.max_health}
        Damage: {self.base_damage}
        Stealth: {self.stealth}
        Charisma: {self.charisma}
        """)
