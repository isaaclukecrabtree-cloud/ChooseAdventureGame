from enemy import Enemy

def create_goblin():
    return Enemy(
        name="Goblin",
        health=5,
        base_damage=2,
    )

def create_ogre():
    return Enemy(
        name = "Ogre",
        health = 10,
        base_damage = 4,
    )

def create_josh():
    return Enemy(
        name = "Josh",
        health = 100,
        base_damage = 100,
    )

def create_demon():
    return Enemy(
        name="Demon",
        health=7,
        base_damage=5,
    )