from events import path_event


def run_game_loop(game_player, max_events=30):
    for i in range(max_events):
        if game_player.health <= 0:
            print("You have died! Game Over.")
            return False

        print(f"\nEvent {i + 1}")
        path_event(game_player)

    print(f"\nCongratulations! You survived all {max_events} events "
          f"with {game_player.health}/{game_player.max_health} HP remaining!")
    return True
