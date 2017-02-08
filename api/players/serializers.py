from rest_framework import serializers
from players.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'cardid', 'profile_picture', 'games_played', 'games_won', 'rating')



class PlayerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'cardid', 'profile_picture')


# Only "owners" can see these fields
class PlayerPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'cardid', 'profile_picture', 'games_played', 'games_won', 'rating')


# Anyone can see these fields
class PlayerPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'profile_picture', 'games_played', 'games_won', 'rating', 'cardid')



# PROTECTED
class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'cardid', 'profile_picture', 'games_played', 'games_won', 'rating')

class MeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'cardid', 'profile_picture')
