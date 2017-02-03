from random import randint
from actions import Action

# TODO: Create real module
class SimulatedHardware:
    def get_next_action(self):
        print "Type in your action!"
        while True:
            try:
                x = str(raw_input("Action: ")).lower().strip()
                break
            except KeyboardInterrupt:
                return Action(Action.EXIT)
            except ValueError:
                print "Not a valid option, type 'h' for help"

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
            return self.get_next_action()
        elif x == "exit":
            return Action(Action.EXIT)
        else:
            print "Not a valid option, type 'h' for help"
            return Action(Action.NONE)
