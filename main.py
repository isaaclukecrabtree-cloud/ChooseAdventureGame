from app import Application
from player import Player
from factory import enemyfactory

def character_create():
    print("Wizard: Hello Traveller, what is your name?")
    player_name = input()
    p = Player(player_name, health=10, damage=1, charisma=1, stealth=0)
    p.set_class_tank()
    return p


    print (f"Wizard: {player.name}, Ygtryal is in grave danger.")
if __name__ == "__main__":
    app = Application()
    player = character_create()
    app.update_player_info(player)
    app.load_event("scene1")
#problem
    app.mainloop()
    app.update_player_info(player)
    scenes = {
        "scene1": {
        "scene_text": "Wizard: Will you help us?.",
        "option1": "Accept Quest",
        "option2": "Ignore him",
        "next1": "scene2",
        "next2": "scene3",
    },

    "scene2": {
        "scene_text": f"Wizard: You accepted my quest! Take these as a token of my appreciation, good luck {player.name}.",
        "option1": "Continue on your journey!",
        "option2": "I changed my mind...",
        "next1": "scene4",
        "next2": "scene1",
    },

    "scene3": {
        "scene_text": f"Wizard: You walk away, you see the wizard shaking his head, disappointed.",
        "option1": "Keep walking.",
        "option2": "I changed my mind.",
        "next1": "scene4",
        "next2": "scene1",

    }}

    app.scenes = scenes






