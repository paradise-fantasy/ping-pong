from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Player(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    cardid = models.CharField(max_length=32, unique=True)
    profile_picture = models.URLField(blank=True, default='')
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)
    rating = models.IntegerField(default=1000)

    def save(self, *args, **kwargs):
        self.cardid = self.cardid.upper()
        super(Player, self).save(*args, **kwargs)
        
    def __str__(self):
        return "%s (%s)" % (self.name, self.cardid)
