import nxppy
import time

mifare = nxppy.Mifare()

def read_card():
    delay = 5

    while True:
        try:
            uid = mifare.select()
            print uid
            time.sleep(delay)
        except nxppy.SelectError:
            # SelectError is raised if no card is in the field.
            pass
        time.sleep(0.2)

read_card()
