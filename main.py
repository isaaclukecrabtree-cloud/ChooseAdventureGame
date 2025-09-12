from player import Player
from factory import enemyfactory

def character_create():
    print("Wizard: Hello Traveller, what is your name?")
    player_name = input()
    p = Player(player_name, health=10, damage=1, charisma=1, stealth=0)
    p.set_class_tank()
    return p


    print (f"Wizard: {player.name}, Ygtryal is in grave danger.")







