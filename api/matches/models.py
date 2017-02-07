from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator
from players.models import Player
from utils.rating import getPotentialRatingGains

# Create your models here.
class Match(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    player_1 = models.ForeignKey(Player, related_name='player_1', on_delete=models.CASCADE)
    player_2 = models.ForeignKey(Player, related_name='player_2', on_delete=models.CASCADE)
    winner = models.IntegerField(choices=((1, 'Player 1'), (2, 'Player 2')))
    score_1 = models.IntegerField(validators=[MinValueValidator])
    score_2 = models.IntegerField(validators=[MinValueValidator])

    def save(self, *args, **kwargs):
        if self.player_1 == self.player_2:
            raise Exception('Player 1 and Player 2 cannot be the same player')

        if (self.winner == 1 and self.score_1 < self.score_2) or (self.winner == 2 and self.score_1 > self.score_2):
            raise Exception('Winner must be the player with the highest score')

        # TODO: Might want to have more edge cases

        try:
            # Update the ratings
            rating_gain = getPotentialRatingGains(self.player_1.rating, self.player_2.rating)
            p1_status = 'wins' if self.winner == 1 else 'loses'
            p2_status = 'wins' if self.winner == 2 else 'loses'
            self.player_1.rating += rating_gain['player_1'][p1_status]
            self.player_2.rating += rating_gain['player_2'][p2_status]

            # Update games played and games won
            self.player_1.games_played += 1
            self.player_2.games_played += 1
            if self.winner == 1:
                self.player_1.games_won += 1
            else:
                self.player_2.games_won += 1

            self.player_1.save()
            self.player_2.save()
        except Exception, e:
            print e

        super(Match, self).save(*args, **kwargs)
