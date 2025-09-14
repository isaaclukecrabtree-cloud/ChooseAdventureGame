from player import Player
from config import CharacterClass, MenuChoices
from util.multichoiceinput import get_multichoice_input
from weapon import WeaponType, Rarity, Weapon
from battle import Battle
from factory import enemyfactory

# region


def choose_class():
    print("\nChoose your class:")
    for menu_option, char_class in MenuChoices.get_class_mapping().items():
        print(f"{menu_option}. {char_class.display_name} - {char_class.description}")

    while True:
        class_choice = input("Enter your choice (1-3): ").strip()
        class_mapping = MenuChoices.get_class_mapping()
        if class_choice in class_mapping:
            return class_mapping[class_choice]
        print("Invalid choice. Please enter 1, 2, or 3.")


def character_create():
    print("Wizard: Hello Traveller, who are you?")
    player_name = input().strip()
    new_player = Player(player_name)

    selected_class = choose_class()
    new_player.set_class(selected_class)

    print(f'''Wizard: Ahh! So you are {player_name} the {new_player.character_class}
    Your character details:
    Name: {new_player.name}
    Class: {new_player.character_class}
    Health: {new_player.health}/{new_player.max_health}
    Damage: {new_player.base_damage}
    Stealth: {new_player.stealth}
    Charisma: {new_player.charisma}''')

    return new_player


def start_game():
    game_player = character_create()

    print(f"Wizard: Well, {game_player.name}, i am afraid now is not a good time,"
          "an evil lurks in the shadows, waiting to destroy everything we know."
          "I wish there was something i could do, alas,"
          "my bones grow old and i am no longer fit for the challenges that await.")

    choice = get_multichoice_input([
        "Offer your assistance to the wizard",
        "Decline the wizard's cry for help",
    ])

    if choice == "1":
        print("The wizard smiles and thanks you for your offer, he hands you a Broken Dagger")
        print("+1 Damage!")
        player_weapon = Weapon(WeaponType.DAGGER, Rarity.BROKEN)
        game_player.charisma += 1
        game_player.equip_weapon(player_weapon)
        valid_answer = True
    elif choice == "2":
        print("Wizard: I understand, this was merely a test of your heart, the quest lies before you nevertheless")
        print("-1 Charisma.")
        game_player.charisma -= 1
        valid_answer = True
    else:
        print("Invalid choice")

# endregion


def test_battle():
    player = Player()
    enemy = enemyfactory.create_josh()
    Battle.start_battle(player, enemy)


if __name__ == "__main__":

    # start_game()

    test_battle()
