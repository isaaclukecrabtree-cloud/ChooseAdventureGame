from lifeform import Lifeform


class Player(Lifeform):
    def __init__(self, name="..."):
        super().__init__(name, 5, 1)
        self.charisma = 0
        self.stealth = 0
        self.character_class = None
        self.equipped_weapon = None

    def set_class(self, character_class):
        self.character_class = character_class
        # Apply all class stats at once
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
