from app import Application
from player import Player
from factory import enemyfactory

def character_create():
    print("Wizard: Hello Traveller, what is your name?")
    player_name = input()
    p = Player(player_name, health=10, damage=1, charisma=1, stealth=0)
    p.set_class_assassin()
    return p


if __name__ == "__main__":
    app = Application()

    demo_event = {
        "scene_text": f".",
        "option1": "Go left",
        "option2": "Go right",
    }


    player = character_create()
    print(f"Welcome {player.base_damage}!")
    app.load_event(demo_event)
    app.update_player_info(player)

    app.mainloop()


