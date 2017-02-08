# -*- coding: utf-8 -*-
import os
import sys
import requests
from threading import Thread
from actions import Action
from hardware import SimulatedHardware
from match import Match

API_HOST = os.environ['API_HOST'] if 'API_HOST' in os.environ else 'localhost'
API_PORT = os.environ['API_PORT'] if 'API_PORT' in os.environ else '8000'
API_URL = 'http://%s:%s' % (API_HOST, API_PORT)

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
        running = True
        while running:
            # TODO: Consider using a buffer for actions
            action = self.hardware.get_next_action()
            print "Got action: " + str(action.type)

            if action.type == Action.EXIT:
                running = False

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

        # Exit program
        print "Game exiting, use CTRL+C to kill the server"


    def start_unranked_match(self):
        print "starting unranked match"

        # Create the match object and start
        self.match = Match(is_ranked=False)
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

        # Broadcast event (PLAYER_[1/2]_[INC/DEC])
        print "Player " + str(player_number) + (" scores!" if increment else " reverts a point.")
        self.socket.emit('GAME_EVENT', {
            'type': 'PLAYER_{0}_SCORE_{1}'.format(player_number, "INC" if increment else "DEC")
        })

        if self.match.state == Match.MATCH_OVER:
            print "Match over!"

            if self.match.is_ranked:
                # Post game to API
                self.post_match()

            # Set correct state
            self.state = Game.STATE_IDLE
            self.player_1 = None
            self.player_2 = None

            # Broadcast event
            self.socket.emit('GAME_EVENT', { 'type': 'MATCH_OVER' })


    def post_match(self):
        print 'Posting match to API'
        id_1 = requests.get('%s/me/%s' % (API_URL, self.player_1)).json()['id']
        id_2 = requests.get('%s/me/%s' % (API_URL, self.player_2)).json()['id']

        data = {
            'player_1': id_1,
            'player_2': id_2,
            'score_1': self.match.player_1.score,
            'score_2': self.match.player_2.score,
            'winner': 1 if self.match.player_1.score > self.match.player_2.score else 2
        }

        requests.post('%s/matches/' % API_URL, json=data)
