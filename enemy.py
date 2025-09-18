from lifeform import Lifeform

class Enemy(Lifeform):
    def stats(self):
        return f"Enemy: {self.name}\nHealth: {self.health}\nDamage: {self.base_damage}\n"

    def scale_to_player_level(self, player_level):
        if player_level <= 1:
            return

        scaling_bonus = self.get_scaling_bonus(player_level)

        health_bonus = scaling_bonus["health"]
        damage_bonus = scaling_bonus["damage"]

        self.health += health_bonus
        self.max_health += health_bonus
        self.base_damage += damage_bonus

    def get_scaling_bonus(self, player_level):
        level_diff = player_level - 1

        scaling_rules = {
            "Goblin": {"health_per_level": 2, "damage_per_level": 1},
            "Ogre": {"health_per_level": 3, "damage_per_level": 2},
            "Josh": {"health_per_level": 1, "damage_per_level": 10},
            "Demon": {"health_per_level": 2, "damage_per_level": 1}
        }

        rule = scaling_rules.get(self.name, scaling_rules["Goblin"])

        return {
            "health": rule["health_per_level"] * level_diff,
            "damage": rule["damage_per_level"] * level_diff
        }