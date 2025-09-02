import random
import tkinter as tk
from foes import Enemy
from weapons import random_weapon, format_weapon
#class Event:
def enemy_event(player):
    print("An enemy appears, prepare to fight!")
    enemy = Enemy("Goblin", health=5, damage=2)

    while player.is_alive() and enemy.is_alive():
        player.attack(enemy)
        if enemy.is_alive():
            enemy.attack(player)
    if player.is_alive():
        print(f"You defeated {enemy.name}!")
        print(player.stats())
    else:
        print("Game Over")

def safe_event(player):
    print("You find a clear and calm area to rest")
    print(f"You awake feeling refreshed.")
    player.heal(3)

def treasure_event(player, new_weapon):
    new_weapon = random_weapon()

    print(f"You found a {format_weapon(new_weapon)}")

    if player.weapon:
        print(f"Current weapon: {format_weapon(player.weapon)}")
    else:
        print("You are currently unarmed.")

    def accept_weapon():
        player.weapon = new_weapon
        print(f"{player.name} equips the {format_weapon(new_weapon)}")
        window.destroy()

    def decline_weapon():
        print(f"{player.name} keeps their current equipment.")
        window.destroy()

    window = tk.Tk()
    window.title("events.py")
    window.attributes("-topmost", True)
    tk.Label(window, text="You found treasure!").pack(pady=100)
    tk.Button(window, text="Equip new weapon.", command=accept_weapon, width=50,
              height=5).pack(side="left", padx=15, pady=15)
    tk.Button(window, text="Keep current weapon.", command=decline_weapon,
              width=50, height=5).pack(side="left", padx=15, pady=15)
    window.mainloop()

def building_event(player):
    print("A seemingly abandoned building can be seen in the distance, do you wish to explore it?")

def random_event(player):
    events = [enemy_event, safe_event, treasure_event, building_event]
    event = treasure_event
    #event = random.choice(events)
    event(player, events)

