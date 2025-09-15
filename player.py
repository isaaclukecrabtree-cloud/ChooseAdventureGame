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

    def set_class(self, character_class):
        self.character_class = character_class
        self.health = character_class.max_health
        self.max_health = character_class.max_health
        self.base_damage = character_class.base_damage
        self.charisma = character_class.charisma
        self.stealth = character_class.stealth

    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon
        print(f"{self.name} picks up the {weapon}")

    def display_stats(self):
        print(f'''Your character details:
        
        Name: {self.name}
        Class: {self.character_class.display_name}
        Health: {self.health}/{self.max_health}
        Damage: {self.base_damage}
        Stealth: {self.stealth}
        Charisma: {self.charisma}
        ''')
