from player import Player
from factory import enemyfactory
from weapons import WeaponType, Rarity, Weapon

def character_create():
    print("Wizard: Hello Traveller, who are you?")
    name = input()
    player = Player(name)

    print(f"Wizard: Ahh! So you are {name} the {player.character_class}")
    return player

if __name__ == "__main__":
    player = character_create()
    print("Your character details:")
    print(f"Name: {player.name}")
    print(f"Class: {player.character_class}")
    print(f"Health: {player.health}/{player.max_health}")
    print(f"Damage: {player.base_damage}")
    print(f"Stealth: {player.stealth}")
    print(f"Charisma: {player.charisma}")

    print(f"Wizard: Well, {player.name}, i am afraid now is not a good time, an evil lurks in the shadows, waiting to destroy everything we know. I wish there was something i could do, alas, my bones grow old and i am no longer fit for the challenges that await.")

    valid_answer = False
    while not valid_answer:
        print("1. Offer your assistance to the wizard")
        print("2. Decline the wizard's cry for help")
        print("3. Stare into the wizards eyes...")


        choice = input("Enter your choice: ")

        if choice == "1":
            print("The wizard smiles and thanks you for your offer, he hands you a Broken Dagger")
            print("+1 Damage!")
            player_weapon = create_weapon(WeaponType.DAGGER, Rarity.BROKEN)
            player.charisma += 1
            player.equip_weapon(("Dagger", 2))
            valid_answer = True
        elif choice == "2":
            print("Wizard: I understand, this was merely a test of your heart, the quest lies before you nevertheless")
            print("-1 Charisma.")
            player.charisma -= 1
            valid_answer = True
        elif choice == "3":
            print("Wizard: ...Can i... Help you?...")
            valid_answer = False

        else:
            print("Invalid choice")





