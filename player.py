from config import CharacterClass
from lifeform import Lifeform


class Player(Lifeform):
    def __init__(self, name="..."):
        super().__init__(name=name,
                         health=5,
                         base_damage=1)
        self.charisma = 0
        self.stealth = 0

        self.character_class = None
        self.weapon = None

    def set_class(self, character_class: CharacterClass):
        self.character_class = character_class.display_name
        self.charisma = character_class.charisma
        self.stealth = character_class.stealth
        self.max_health = character_class.max_health
        self.health = self.max_health

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} picks up the {weapon}")
