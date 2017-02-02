# -*- coding: utf-8 -*-
from threading import Thread
from actions import Action
from hardware import SimulatedHardware
from match import Match

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
                    self.register_player(card_id=action.data)

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
        self.player_1 = None
        self.player_2 = None
        self.match.start(self.player_1, self.player_2)

        # Set correct state
        self.state = Game.STATE_IN_GAME

        # Broadcast event
        self.socket.emit('GAME_EVENT', { 'type': 'NEW_UNRANKED_MATCH_STARTED', 'date': self.match.date.isoformat() })


    def start_ranked_match(self):
        print "starting ranked match"

        # Create the match object and start
        self.match = Match()
        self.match.start(self.player_1, self.player_2)

        # Set correct state
        self.state = Game.STATE_IN_GAME

        # Broadcast event
        self.socket.emit('GAME_EVENT', { 'type': 'NEW_MATCH_STARTED', 'date': self.match.date.isoformat() })


    def cancel_match(self):
        print "cancelling current match"

        # Delete the current match object
        del self.match

        # Set correct state
        self.state = Game.STATE_IDLE
        self.player_1 = None
        self.player_2 = None

        # Broadcast event
        self.socket.emit('GAME_EVENT', { 'type': 'MATCH_CANCELLED' })


    def register_player(self, card_id):
        print card_id
        print "Registering player with card_id: " + str(card_id)

        # TODO: Fetch players from API
        if not self.player_1:

            # Set player_1
            self.player_1 = card_id

            # Broadcast event
            self.socket.emit('GAME_EVENT', { 'type': 'PLAYER_1_JOINED', 'cardId': self.player_1 })

            # TODO: Timeout when no second player joins for X seconds

        elif self.player_1 == card_id:
            # Player is already registered
            pass

        else:
            # Set player_2
            self.player_2 = card_id

            # Broadcast event
            self.socket.emit('GAME_EVENT', { 'type': 'PLAYER_2_JOINED', 'cardId': self.player_2 })

            # Start the match
            self.start_ranked_match()


    def update_score(self, player_number, increment=True):
        # TODO: Try-catch for reverting below 0
        self.match.update_score(player_number, increment)

        if self.match.state == Match.MATCH_OVER:
            print "Match over!"
            # TODO: Update ratings

            # Set correct state
            self.state = Game.STATE_IDLE
            self.player_1 = None
            self.player_2 = None

            # Broadcast event
            self.socket.emit('GAME_EVENT', { 'type': 'MATCH_OVER' })

        else:
            # Broadcast event (PLAYER_[1/2]_[INC/DEC])
            print "Player " + str(player_number) + (" scores!" if increment else " reverts a point.")
            self.socket.emit('GAME_EVENT', {
                'type': 'PLAYER_{0}_SCORE_{1}'.format(player_number, "INC" if increment else "DEC")
            })
