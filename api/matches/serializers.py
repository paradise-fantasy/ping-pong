from rest_framework import serializers
from matches.models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'player_1', 'player_2', 'winner', 'score_1', 'score_2')
