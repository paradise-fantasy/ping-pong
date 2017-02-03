class Action:
    NONE, \
    BUTTON_1_PRESS, \
    BUTTON_2_PRESS, \
    BUTTON_1_LONG_PRESS, \
    BUTTON_2_LONG_PRESS, \
    BOTH_BUTTONS_LONG_PRESS, \
    CARD_SWIPE, \
    EXIT \
        = range(8)

    def __init__(self, type, data=None):
        if type not in range(8):
            raise ValueError("Actions must have a valid Action type")
        self.type = type
        self.data = data
