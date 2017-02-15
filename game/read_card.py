import nxppy
from actions import Action
import time

mifare = nxppy.Mifare()

def read_card(hardware):
    delay = 2 # In order not to scan same card twice

    while hardware.running:
        try:
            uid = mifare.select()
            action = Action( Action.CARD_SWIPE, uid )
            hardware.insert_action(action)
            time.sleep(delay)
        except nxppy.SelectError:
            # SelectError is raised if no card is in the field.
            pass
        time.sleep(0.2)
