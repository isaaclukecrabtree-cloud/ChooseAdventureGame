from event import Event
from player import Player
import weaponfactory

def start_event():
    return Event(
        text="Wizard: Will you help us?.",
        option1_text="Accept Quest",
        option2_text="Ignore him",
        option1_action=start_event_accept,
        option2_action=start_event_ignore
    )
def start_event_accept(player):
    player.charisma += 1
    player.equip_weapon(weaponfactory.create_dagger())
def start_event_ignore(player):
    player.charisma -= 1