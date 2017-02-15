import eventlet
from actions import Action
from read_card import read_card
from read_buttons import read_buttons

class Hardware():
    def __init__(self):
        self.running = False
        self.actions = []

    def get_next_action(self):
        if len(self.actions) == 0:
            return Action(Action.NONE)
        return self.actions.pop(0)

    def insert_action(self, action):
        self.actions.append(action)

    def start(self):
        self.running = True
        eventlet.spawn_n(read_card, self)
        eventlet.spawn_n(read_buttons, self)
