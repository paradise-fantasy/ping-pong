#!/usr/bin/python

from RPi import GPIO
from time import time, sleep
from actions import Action

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(40,GPIO.IN, pull_up_down=GPIO.PUD_UP)


LONG_PRESS_THRESHOLD = 3

last_btn1 = 0
last_btn2 = 0
hold_btn1 = False
hold_btn2 = False
both_already_held = False

while True:
    btn1 = 1 - GPIO.input(37) # 0 if up, 1 if down
    btn2 = 1 - GPIO.input(40) # 0 if up, 1 if down

    # print "states " + btn1 + ", " + btn2

    if btn1 and not last_btn1:
        print "green down"
        last_btn1_event = time()

    if btn2 and not last_btn2:
        print "red down"
        last_btn2_event = time()

    if btn1 and not hold_btn1:
        delta = time() - last_btn1_event
        if (delta > LONG_PRESS_THRESHOLD):
            hold_btn1 = True
            print "green long press"

    if btn2 and not hold_btn2:
        delta = time() - last_btn2_event
        if (delta > LONG_PRESS_THRESHOLD):
            hold_btn2 = True
            print "red long press"

    if last_btn1 and not btn1:
        if not hold_btn1:
            print "green press"
        hold_btn1 = False
        both_already_held = False

    if last_btn2 and not btn2:
        if not hold_btn2:
            print "red press"
        hold_btn2 = False
        both_already_held = False

    if not both_already_held and hold_btn1 and hold_btn2:
        print "both buttons long press"
        both_already_held = True

    last_btn1, last_btn2 = btn1, btn2
    sleep(0.25)
