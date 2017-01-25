import datetime
from player import *

GAME_NOT_STARTED = "not_started"
GAME_IN_PROGRESS = "in_progress"
GAME_OVER = "over"
GAME_CANCELLED = "cancelled"

class MatchException(Exception):
    pass

class Match:
    def __init__(self):
        self.state = GAME_NOT_STARTED

    def __str__(self):
        output = " MATCH SCORE ".center(41, "#") + "\n"
        output += "   {0}".format(self.player_1.name).ljust(17)
        output += "{0} - {1}".format(self.player_1.score, self.player_2.score).center(7)
        output += "{0}   ".format(self.player_2.name).rjust(17)
        output += "\n"
        output += "".center(41, "#")
        return output

    def start(self, player_1, player_2):
        self.state = GAME_IN_PROGRESS
        self.date = datetime.datetime.now()
        self.player_1 = MatchPlayer(player_1)
        self.player_2 = MatchPlayer(player_2)

    def update_score(self, player_number, increment = True):
        if not self.state == GAME_IN_PROGRESS:
            raise MatchException("Game is not in progress")

        # Elect player and opponent given player_number
        player = self.player_1 if player_number == 1 else self.player_2
        opponent = self.player_2 if player_number == 1 else self.player_1

        # Evaluate new score
        new_score = player.score + (1 if increment else -1)
        if new_score < 0:
            raise MatchException("Player " + player_number + " cannot have the score: " + new_score)

        # Update score
        player.score = new_score

        # Evaluate match
        if player.score >= 11 and player.score > opponent.score + 1:
            # Game over
            self.state = GAME_OVER
            self.winner = player

    def cancel_match(self):
        self.state = GAME_CANCELLED


class MatchPlayer(Player):
    def __init__(self, player):
        self.name = player.name
        self.score = 0
