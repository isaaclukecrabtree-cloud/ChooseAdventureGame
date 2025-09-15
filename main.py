from gamesetup import start_game
from gameloop import run_game_loop


def main():
    game_player = start_game()
    run_game_loop(game_player, max_events=10)


if __name__ == "__main__":
    main()
