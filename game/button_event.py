#!/usr/bin/python

from RPi import GPIO
from time import sleep
from actions import Action

def button_event(hardware)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(37,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(40,GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while hardware.running:
        greenBtn = GPIO.input(37)
        redBtn = GPIO.input(40)
        while (greenBtn):
            greenBtn = GPIO.input(37)
            action = Action( Action.BUTTON_1_PRESS )
            sleep(0.25)
        while (greenBtn):
            redBtn = GPIO.input(40)
            action = Action( Action.BUTTON_2_PRESS )
            sleep(0.25)
        hardware.insert_action(action)
