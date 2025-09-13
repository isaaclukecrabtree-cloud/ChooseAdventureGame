from config import CharacterClass
from lifeform import Lifeform
class Player(Lifeform):
    def __init__(self, name):
        super().__init__(name, 1, 0)  # Temporary values
        self.character_class = None
        self.max_health = 0
        self.base_damage = 0
        self.charisma = 0
        self.stealth = 0
        self.weapon = None

    def set_class(self, character_class: CharacterClass):
        self.character_class = character_class.display_name
        self.base_damage = character_class.base_damage
        self.charisma = character_class.charisma
        self.stealth = character_class.stealth
        self.max_health = character_class.max_health
        self.health = self.max_health

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} picks up the {weapon}")