from rest_framework import generics
from .models import LeagueUser, Team, Game
from .serializers import LeagueUserSerializer, TeamSerializer, GameSerializer

class LeagueUserAPIView(generics.ListCreateAPIView):
    queryset = LeagueUser.objects.all()
    serializer_class = LeagueUserSerializer

class TeamAPIView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class GameAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
