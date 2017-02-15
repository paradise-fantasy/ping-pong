#!/usr/bin/python

from RPi import GPIO
import eventlet
from time import time
from actions import Action

def read_buttons(hardware):
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(37,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(40,GPIO.IN, pull_up_down=GPIO.PUD_UP)

    LONG_PRESS_THRESHOLD = 3
    HOLD_EVENTS = False

    last_btn1 = 0
    last_btn2 = 0

    while hardware.running:
        btn1 = GPIO.input(37) # 0 if up, 1 if down
        btn2 = GPIO.input(40) # 0 if up, 1 if down

        action = '' #reset actions from last iteration

        # print "states " + btn1 + ", " + btn2

        if btn1 and not last_btn1:
            #print "green down"
            last_btn1_event = time()

        if btn2 and not last_btn2:
            #print "red down"
            last_btn2_event = time()
    
        if last_btn1 and not btn1 and not HOLD_EVENTS:
            delta = time() - last_btn1_event
            if delta > LONG_PRESS_THRESHOLD:
                #print "green long press"
                action = Action( Action.BUTTON_2_LONG_PRESS )
                hardware.insert_action(action)
            else:
                #print "green press"
                action = Action( Action.BUTTON_2_PRESS )
                hardware.insert_action(action)

        if last_btn2 and not btn2 and not HOLD_EVENTS:
            delta = time() - last_btn2_event
            if delta > LONG_PRESS_THRESHOLD:
                #print "red long press"
                action = Action( Action.BUTTON_1_LONG_PRESS )
                hardware.insert_action(action)
            else:
                #print "red press"
                action = Action( Action.BUTTON_1_PRESS )
                hardware.insert_action(action)
    
        if last_btn1 and last_btn2:
            delta1 = time() - last_btn1_event
            delta2 = time() - last_btn2_event
            if delta1 > LONG_PRESS_THRESHOLD and delta2 > LONG_PRESS_THRESHOLD:
                if not HOLD_EVENTS:
                    #print "both long press"
                    action = Action( Action.BOTH_BUTTONS_LONG_PRESS )
                    hardware.insert_action(action)
                    HOLD_EVENTS = True
        if btn1 == btn2 == last_btn1 == last_btn2 == 0:
            HOLD_EVENTS = False
    
        last_btn1, last_btn2 = btn1, btn2
        eventlet.sleep(0.1)
