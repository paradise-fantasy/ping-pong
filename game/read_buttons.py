#!/usr/bin/python

from RPi import GPIO
import eventlet
from time import time
from actions import Action

def read_buttons(hardware):
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(37,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(40,GPIO.IN, pull_up_down=GPIO.PUD_UP)

    LONG_PRESS_THRESHOLD = 1.5

    last_btn1 = 0
    last_btn2 = 0
    hold_btn1 = False
    hold_btn2 = False
    both_already_held = False

    while hardware.running:
        btn1 = 1 - GPIO.input(37) # 0 if up, 1 if down
        btn2 = 1 - GPIO.input(40) # 0 if up, 1 if down

        action = '' #reset actions from last iteration

        # print "states " + btn1 + ", " + btn2
        if btn1 and not last_btn1:
            last_btn1_event = time()

        if btn2 and not last_btn2:
            last_btn2_event = time()

        if btn1 and not hold_btn1:
            delta = time() - last_btn1_event
            if (delta > LONG_PRESS_THRESHOLD):
                hold_btn1 = True
                action = Action( Action.BUTTON_1_LONG_PRESS )
                hardware.insert_action(action)

        if btn2 and not hold_btn2:
            delta = time() - last_btn2_event
            if (delta > LONG_PRESS_THRESHOLD):
                hold_btn2 = True
                action = Action( Action.BUTTON_2_LONG_PRESS )
                hardware.insert_action(action)

        if last_btn1 and not btn1:
            if not hold_btn1:
                action = Action( Action.BUTTON_1_PRESS )
                hardware.insert_action(action)
            hold_btn1 = False
            both_already_held = False

        if last_btn2 and not btn2:
            if not hold_btn2:
                action = Action( Action.BUTTON_2_PRESS )
                hardware.insert_action(action)
            hold_btn2 = False
            both_already_held = False

        if not both_already_held and hold_btn1 and hold_btn2:
            action = Action( Action.BOTH_BUTTONS_LONG_PRESS )
            hardware.insert_action(action)
            both_already_held = True

        last_btn1, last_btn2 = btn1, btn2
        eventlet.sleep(0.1)
