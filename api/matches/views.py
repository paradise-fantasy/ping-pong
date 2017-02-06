from django.shortcuts import render

# Create your views here.
from matches.models import Match
from matches.serializers import MatchSerializer
from rest_framework import generics

# TODO: Protect 'POST' api
class MatchList(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

# TODO: Protect Update and Destroy
class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
