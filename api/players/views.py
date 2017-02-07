from django.shortcuts import render

# Create your views here.
from players.models import Player
from players import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from utils.rating import getPotentialRatingGains


# OPEN API
class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.PlayerPostSerializer
        return serializers.PlayerPublicSerializer


class PlayerDetail(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = serializers.PlayerPublicSerializer


class PlayerRatingPotential(APIView):
    def get(self, request, player_key_1, player_key_2, format=None):
        try:
            player_1 = Player.objects.get(pk=player_key_1)
        except Player.DoesNotExist:
            raise Http404

        try:
            player_2 = Player.objects.get(pk=player_key_2)
        except Player.DoesNotExist:
            raise Http404

        rating_1 = player_1.rating
        rating_2 = player_2.rating

        potential_gains = getPotentialRatingGains(rating_1, rating_2)
        return Response(potential_gains)


# PROTECTED API
# TODO: Protect this!
class MeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    lookup_field = 'cardid'

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return serializers.MeUpdateSerializer
        return serializers.MeSerializer
