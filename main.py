from player import Player
from factory import enemyfactory

def character_create():
    print("Wizard: Hello Traveller, who are you?")
    name = input()
    player = Player(name)

    classes= {
        "1": ("Warrior",
    player.set_class_warrior),
        "2": ("Assassin",
    player.set_class_assassin),
        "3": ("Tank",
    player.set_class_tank),
    }

    print("Choose your class")
    for key, (class_name, _) in classes.items():
        print(f"{key}. {class_name}")

    choice = None
    while choice not in classes:
        choice = input("Enter your choice: ")
        if choice not in classes:
            print("Invalid choice")

    class_name, class_method = classes[choice]
    class_method()

    print(f"Wizard: Ahh! So you are {name} the {player.character_class}")
    return player

if __name__ == "__main__":
    character = character_create()
    print("Your character details:")
    print(f"Name: {character.name}")
    print(f"Class: {character.character_class}")
    print(f"Health: {character.health}/{character.max_health}")
    print(f"Damage: {character.base_damage}")
    print(f"Stealth: {character.stealth}")
    print(f"Charisma: {character.charisma}")

    print(f"Wizard: Well, {character.name}, i am afraid now is not a good time, an evil lurks in the shadows, waiting to destroy everything we know. I wish there was something i could do, alas, my bones grow old and i am no longer fit for the challenges that await.")

    valid_answer = False
    while not valid_answer:
        print("1. Offer your assistance to the wizard")
        print("2. Decline the wizard's cry for help")
        print("3. Stare into the wizards eyes...")


        choice = input("Enter your choice: ")

        if choice == "1":
            print("The wizard smiles and thanks you for your offer, he hands you a Broken Dagger")
            print("+1 Damage!")
            valid_answer = True
        elif choice == "2":
            print("Wizard: I understand, this was merely a test of your heart, the quest lies before you nevertheless")
            print("-1 Charisma.")
            character.charisma -= 1
            valid_answer = True
        elif choice == "3":
            print("Wizard: ...Can i... Help you?...")
            valid_answer = False

        else:
            print("Invalid choice")

