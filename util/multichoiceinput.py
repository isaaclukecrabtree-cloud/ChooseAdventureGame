def get_multichoice_input(options):
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    return get_valid_integer(len(options))

def get_valid_integer(range):
    while True:
        try:
            choice = int(input(f"Choose (1-{range}): "))
            if choice < 1 or choice > range:
                pass
            else:
                return str(choice)
        except:
            print("Please enter a valid number.")