from enemy import Enemy

def create_goblin():
    return Enemy(
        name="Goblin",
        health=5,
        damage=2,
    )

def create_ogre():
    return Enemy(
        name = "Ogre",
        health = 10,
        damage = 4,
    )

def create_josh():
    return Enemy(
        name = "Josh",
        health = 100,
        damage = 100,
    )

def create_demon():
    return Enemy(
        name="Demon",
        health=7,
        damage=5,
    )