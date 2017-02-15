import eventlet
import nxppy
from actions import Action

mifare = nxppy.Mifare()

def read_card(hardware):
    delay = 2 # In order not to scan same card twice
    while hardware.running:
        try:
            uid = mifare.select()
            action = Action( Action.CARD_SWIPE, uid )
            hardware.insert_action(action)
            eventlet.sleep(delay)
        except nxppy.SelectError:
            # SelectError is raised if no card is in the field.
            pass
        eventlet.sleep(0.2)
