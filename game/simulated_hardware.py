import thread
from random import randint
from actions import Action

class SimulatedHardware():
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
        thread.start_new_thread(self.threaded, ())

    def threaded(self):
        while self.running:
            try:
                action = self.read_action()
                self.insert_action(action)
            except KeyboardInterrupt:
                self.insert_action(Action(Action.EXIT))
                self.running = False
            except ValueError:
                print "Not a valid option, type 'h' for help"

    def read_action(self):
        print "Type in your action!"
        x = str(raw_input("Action: ")).lower().strip()

        if x == "1":
            return Action(Action.BUTTON_1_PRESS)
        elif x == "2":
            return Action(Action.BUTTON_2_PRESS)
        elif x == "11":
            return Action(Action.BUTTON_1_LONG_PRESS)
        elif x == "22":
            return Action(Action.BUTTON_2_LONG_PRESS)
        elif x == "3":
            return Action(Action.BOTH_BUTTONS_LONG_PRESS)
        elif x == "x":
            return Action(Action.CARD_SWIPE, str(randint(1, 9)) )
        elif x == "h":
            print "The following actions can be input:\n1:\tButton 1 pressed\n2:\tButton 2 pressed\n11:\tButton 1 pressed long\n22:\tButton 2 pressed long\n3:\tBoth buttons pressed long\nx:\tCard swiped (random data created)\nexit:\tExits the program\nh:\tShow this information\n"
            return self.read_action()
        elif x == "exit":
            self.running = False
            return Action(Action.EXIT)
        else:
            print "Not a valid option, type 'h' for help"
            return Action(Action.NONE)
