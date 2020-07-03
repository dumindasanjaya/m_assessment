from rest_framework import serializers

from .models import LeagueUser, Team, Game

class LeagueUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueUser
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
