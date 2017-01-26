# -*- coding: utf-8 -*-
from threading import Thread
from actions import Action
from hardware import SimulatedHardware
from match import Match
from player import Player

# TODO: Get from API
players = {
    "1": {
        "name": u"Raymi"
    },
    "2": {
        "name": u"Håvard"
    },
    "3": {
        "name": u"Frederik"
    },
    "4": {
        "name": u"Kabbe"
    },
    "5": {
        "name": u"Tormod"
    }
}

class Game(Thread):
    STATE_IDLE, STATE_IN_GAME = range(2)

    def __init__(self, socket):
        Thread.__init__(self)
        self.state = Game.STATE_IDLE
        self.socket = socket
        self.hardware = SimulatedHardware()
        self.match = None
        self.player_1 = None
        self.player_2 = None

    def run(self):
        while True:
            # TODO: Consider using a buffer for actions
            action = self.hardware.get_next_action()
            print "Got action: " + str(action.type)

            if self.state == Game.STATE_IDLE:
                if action.type == Action.BOTH_BUTTONS_LONG_PRESS:
                    self.start_unranked_match()

                if action.type == Action.CARD_SWIPE:
                    self.register_player(action.data)

            elif self.state == Game.STATE_IN_GAME:
                if action.type == Action.BUTTON_1_PRESS:
                    self.update_score(player_number=1)

                if action.type == Action.BUTTON_2_PRESS:
                    self.update_score(player_number=2)

                if action.type == Action.BUTTON_1_LONG_PRESS:
                    self.update_score(player_number=1, increment=False)

                if action.type == Action.BUTTON_2_LONG_PRESS:
                    self.update_score(player_number=2, increment=False)

                if action.type == Action.BOTH_BUTTONS_LONG_PRESS:
                    self.cancel_match()


    def start_unranked_match(self):
        print "starting unranked match"

        # Create the match object and start
        self.match = Match()
        self.player_1 = Player("", "Anonymouse 1")
        self.player_2 = Player("", "Anonymouse 2")
        self.match.start(self.player_1, self.player_2)

        # Set correct state
        self.state = Game.STATE_IN_GAME

        # Broadcast event
        self.socket.emit('NEW_MATCH_STARTED', self.match.to_dict())


    def start_ranked_match(self):
        print "starting ranked match"

        # Create the match object and start
        self.match = Match()
        self.match.start(self.player_1, self.player_2)

        # Set correct state
        self.state = Game.STATE_IN_GAME

        # Broadcast event
        self.socket.emit('NEW_MATCH_STARTED', self.match.to_dict())


    def cancel_match(self):
        print "cancelling current match"

        # Delete the current match object
        del self.match

        # Set correct state
        self.state = Game.STATE_IDLE
        self.player_1 = None
        self.player_2 = None

        # Broadcast event
        self.socket.emit('MATCH_CANCELLED')


    def register_player(self, player_data):
        card_id = player_data["card_id"]
        name = players[card_id]["name"]

        print "Registering player with card_id: " + card_id

        # TODO: Fetch players from API
        if not self.player_1:

            # Set player_1
            self.player_1 = Player(card_id, name)

            # Broadcast event
            self.socket.emit("PLAYER_1_JOINED", self.player_1.to_dict())

            # TODO: Timeout when no second player joins for X seconds

        elif self.player_1.card_id == card_id:
            # Player is already registered
            pass

        else:
            # Set player_2
            self.player_2 = Player(card_id, name)

            # Start a ranked match, this method handles broadcasting
            self.start_ranked_match()


    def update_score(self, player_number, increment=True):
        # TODO: Implement update score
        self.match.update_score(player_number, increment)

        if self.match.state == Match.GAME_OVER:
            # TODO: Update ratings

            # Set correct state
            self.state = Game.STATE_IDLE
            self.player_1 = None
            self.player_2 = None

            # Broadcast event
            self.socket.emit("GAME_OVER", self.match.to_dict())

        else:
            # Broadcast event (PLAYER_[1/2]_[INC/DEC])
            self.socket.emit("PLAYER_{0}_SCORE_{1}".format(player_number, "INC" if increment else "DEC"), self.match.to_dict())