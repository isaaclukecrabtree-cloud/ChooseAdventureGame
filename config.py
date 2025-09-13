from enum import Enum


class CharacterClass(Enum):
    ASSASSIN = ("Assassin", 2, 1, 4, 6, "High stealth, low health")
    WARRIOR = ("Warrior", 3, 1, 1, 9, "Balanced stats")
    TANK = ("Tank", 1, 1, 0, 13, "High health, low damage")

    def __init__(self, display_name, base_damage, charisma, stealth, max_health, description):
        self.display_name = display_name
        self.base_damage = base_damage
        self.charisma = charisma
        self.stealth = stealth
        self.max_health = max_health
        self.description = description


class MenuChoices:
    ASSASSIN = "1"
    WARRIOR = "2"
    TANK = "3"

    @classmethod
    def get_class_mapping(cls):
        return {
            cls.ASSASSIN: CharacterClass.ASSASSIN,
            cls.WARRIOR: CharacterClass.WARRIOR,
            cls.TANK: CharacterClass.TANK

        }