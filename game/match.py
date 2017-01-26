import datetime
from player import *

class MatchException(Exception):
    pass

class Match:
    GAME_NOT_STARTED,\
    GAME_IN_PROGRESS,\
    GAME_OVER,\
    GAME_CANCELLED\
    = range(4)

    def __init__(self):
        self.state = Match.GAME_NOT_STARTED

    def __str__(self):
        output = " MATCH SCORE ".center(41, "#") + "\n"
        output += "   {0}".format(self.player_1.name).ljust(17)
        output += "{0} - {1}".format(self.player_1.score, self.player_2.score).center(7)
        output += "{0}   ".format(self.player_2.name).rjust(17)
        output += "\n"
        output += "".center(41, "#")
        return output

    def start(self, player_1, player_2):
        self.state = Match.GAME_IN_PROGRESS
        self.date = datetime.datetime.now()
        self.player_1 = MatchPlayer(player_1)
        self.player_2 = MatchPlayer(player_2)

    def update_score(self, player_number, increment = True):

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
            self.state = Match.GAME_OVER

    def cancel_match(self):
        self.state = Match.GAME_CANCELLED

    def to_dict(self):
        return {
            "state": self.state,
            "date": self.date.isoformat(),
            "player_1": self.player_1.to_dict(),
            "player_2": self.player_2.to_dict()
        }


class MatchPlayer(Player):
    def __init__(self, player):
        self.name = player.name
        self.score = 0

    def to_dict(self):
        return {
            "name": self.name,
            "score": self.score
        }
