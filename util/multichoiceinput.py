def get_multichoice_input(options):
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    return get_valid_integer(len(options))


def get_valid_integer(length):
    while True:
        try:
            choice = int(input(f"Enter choice (1-{length}): "))

            if choice in range(length):
                return choice

            print("Enter a valid number.")

        except:
            pass
