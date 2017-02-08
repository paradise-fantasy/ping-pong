import datetime

class MatchException(Exception):
    pass

class Match:
    MATCH_NOT_STARTED,\
    MATCH_IN_PROGRESS,\
    MATCH_OVER,\
    MATCH_CANCELLED\
    = range(4)

    def __init__(self, is_ranked=True):
        self.state = Match.MATCH_NOT_STARTED
        self.is_ranked = is_ranked

    def __str__(self):
        output = " MATCH SCORE ".center(41, "#") + "\n"
        output += "   {0}".format(self.player_1.name).ljust(17)
        output += "{0} - {1}".format(self.player_1.score, self.player_2.score).center(7)
        output += "{0}   ".format(self.player_2.name).rjust(17)
        output += "\n"
        output += "".center(41, "#")
        return output

    def start(self, card_id_1, card_id_2):
        self.state = Match.MATCH_IN_PROGRESS
        self.date = datetime.datetime.now()
        self.player_1 = MatchPlayer(card_id_1)
        self.player_2 = MatchPlayer(card_id_2)

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
            self.state = Match.MATCH_OVER

    def cancel_match(self):
        self.state = Match.MATCH_CANCELLED

class MatchPlayer:
    def __init__(self, card_id):
        self.card_id = card_id
        self.score = 0
