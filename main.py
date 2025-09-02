from app import Application
from player import Player

if __name__ == "__main__":
    app = Application()

    # Example usage
    demo_event = {
        "scene_text": "You are standing in a dark forest...",
        "option1": "Go left",
        "option2": "Go right",
        "character_name": "Alice",
        "level": 3
    }

    player = Player(
        name="Ninja",
        health=100,
        damage=10,
        charisma=10,
        stealth=0,
    )

    app.load_event(demo_event)
    app.update_player_info(player)

    app.mainloop()

