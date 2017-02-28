# -*- coding: utf-8 -*-
import os
import sys
from time import time
import eventlet
import requests
from actions import Action
from match import Match, MatchException

USE_SIMULATED_HARDWARE = os.environ['USE_SIMULATED_HARDWARE'] if 'USE_SIMULATED_HARDWARE' in os.environ else False
print USE_SIMULATED_HARDWARE
API_HOST = os.environ['API_HOST'] if 'API_HOST' in os.environ else 'localhost'
API_PORT = os.environ['API_PORT'] if 'API_PORT' in os.environ else '8000'
API_URL = 'http://%s:%s' % (API_HOST, API_PORT)

MATCH_SETUP_TIMEOUT = 3 # Seconds ...

class Game:
    STATE_IDLE, STATE_IN_GAME = range(2)

    def __init__(self, socket):
        self.state = Game.STATE_IDLE
        self.socket = socket
        if USE_SIMULATED_HARDWARE:
            from simulated_hardware import SimulatedHardware
            self.hardware = SimulatedHardware()
        else:
            from hardware import Hardware
            self.hardware = Hardware()
        self.match = None
        self.player_1 = None
        self.player_2 = None
        self.match_setup_start = None

    def start(self):
        eventlet.spawn_n(self.hardware.start)
        running = True
        while running:
            eventlet.sleep(0.2) # Important!

            # Check if match setup timed out
            if (self.match_setup_start):
                delta = time() - self.match_setup_start
                if (delta >= MATCH_SETUP_TIMEOUT):
                    self.timeout_match()

            # Get next action
            action = self.hardware.get_next_action()
            if action.type == Action.NONE:
                continue

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
        print "Registering player with card_id: %s" % card_id

        # Check if player card ID exists in API
        r = requests.get('%s/me/%s' % (API_URL, card_id))
        if r.status_code == 404:
            print "No player found for card_id %s" % card_id
            self.socket.emit('GAME_EVENT', { 'type': 'PLAYER_NOT_REGISTERED', 'cardId': card_id })
            return

        if r.status_code != 200:
            print "Error: %s when looking up card_id %s in API" % (r.status_code, card_id)
            return

        # TODO: Fetch players from API
        if not self.player_1:

            # Set player_1
            self.player_1 = card_id

            # Set match setup start timestamp
            self.match_setup_start = time()

            # Broadcast event
            self.socket.emit('GAME_EVENT', { 'type': 'PLAYER_1_JOINED', 'cardId': self.player_1 })

            # TODO: Timeout when no second player joins for X seconds

        elif self.player_1 == card_id:
            # Player is already registered
            pass

        else:
            # Set player_2
            self.player_2 = card_id

            # Remove match setup start timestamp
            self.match_setup_start = None

            # Broadcast event
            self.socket.emit('GAME_EVENT', { 'type': 'PLAYER_2_JOINED', 'cardId': self.player_2 })

            # Start the match
            self.start_ranked_match()

    def timeout_match(self):
        print "Match setup timed out"
        self.player_1 = None
        self.match_setup_start = None
        self.socket.emit('GAME_EVENT', { 'type': 'MATCH_SETUP_EXPIRED' })

    def update_score(self, player_number, increment=True):
        try:
            self.match.update_score(player_number, increment)
        except MatchException as error:
            print error
            return

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
