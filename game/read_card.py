import subprocess
from actions import Action
import time

def read_card(hardware):
    last_scan = ['','', time.time()]
    delay = 5

    while hardware.running:
    	proc = subprocess.Popen("explorenfc-basic", stdout=subprocess.PIPE, shell=True)
    	(rfid, error) = proc.communicate()
        if not error:
        	rfid_array = rfid.split(":")
        	current_scan  = [rfid_array[-2][-3:].strip(), rfid_array[-1].strip(), time.time()]
            action = Action( Action.CARD_SWIPE, current_scan[1] )
            if ( last_scan[1] == current_scan[1] ): # Same card as last scan?
                if ( current_scan[2] < last_scan[2] + delay ): # Avoid spamming same card
                    pass
                else:
                    hardware.insert_action(action)
                    last_scan = list(current_scan)
            else: # New card
                hardware.insert_action(action)
                last_scan = list(current_scan)
        else:
            print str(error)
