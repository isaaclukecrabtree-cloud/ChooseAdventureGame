from player import Player
from foes import Enemy
from weapons import Weapon, Colours, format_weapon
import events
import tkinter as tk

print("Wizard: Hello Traveller, what is your name?")
player_name = input()
player = Player(player_name, health=10, damage=1, charisma=1, stealth=0)
print(f"Wizard: Hello {player_name}, our lands have been plagued by evil.You may be our last hope to save this mortal realm.")
print(f"Wizard: Ygtryal needs your help")

def accept():
    window.destroy()
    print(f"{player_name}: I accept your quest to save Ygtryal!")
    print(f"Wizard: Oh {player_name}, your kindness is truly appreciated in this time of need, please take this 'dagger' as a token of my gratitude, farewell!")
    print("Charisma +1!")
    player.charisma += 1
    broken_dagger = Weapon(
        name = "Dagger",
        rarity = "Broken",
        damage = 1,
        colour =Colours.red
    )
    player.weapon = broken_dagger
    print(f"{player_name} now wields {format_weapon(player.weapon)}")
def decline():
    window.destroy()
    print(f"{player_name}: I decline this request.")
    print("Wizard: Our time of peril comes and you decline, your quest begins nonetheless. Goodbye traveller")
    print("Charisma -1...")
    player.charisma -= 1

window = tk.Tk()
window.title("main.py")
window.attributes("-topmost", True)
tk.Label(window, text="Do you Accept or Decline").pack(pady=100)
tk.Button(window, text="I accept your quest to save Ygtryal!", command=accept, width=50, height=5).pack(side="left", padx=15, pady=15)
tk.Button(window, text="I decline this request.", command=decline, width=50, height=5).pack(side="left", padx=15, pady=15)
window.mainloop()

print("As you head on with your journey, you see a fork in the path ahead.")

def left1():
    window.destroy()
    events.random_event(player)
def right1():
    window.destroy()
    events.random_event(player)

window = tk.Tk()
window.title("main.py")
window.attributes("-topmost", True)
tk.Label(window, text="A fork appears, choose your fate").pack(pady=100)
tk.Button(window, text="Head left, the path looks thick with overgrown foliage.", command=left1, width=50, height=5).pack(side="left", padx=15, pady=15)
tk.Button(window, text="Turn right, you hear strange sounds but the path seems safe enough.", command=right1, width=50, height=5).pack(side="left", padx=15, pady=15)
window.mainloop()

