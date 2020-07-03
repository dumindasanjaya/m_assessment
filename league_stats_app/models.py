from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField("name of team", "name", max_length=255)
    createdAt = models.DateTimeField("Created At", auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField("Updated At", auto_now_add=True, null=True, blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.typeName

    class Meta:
        db_table = "team"

class Game(models.Model):
    name = models.CharField("name of game", "name", max_length=255)
    gameDateTime = models.DateTimeField("game date", null=True, blank=True)
    homeTeam = models.ForeignKey(Team, related_name="home_team_id", on_delete=models.CASCADE)
    awayTeam = models.ForeignKey(Team, related_name="away_team_id", on_delete=models.CASCADE)
    homeTeamScore = models.IntegerField(blank=True, null=True)
    awayTeamScore = models.IntegerField(blank=True, null=True)
    wonByTeam = models.ForeignKey(Team, related_name="won_by_team_id", on_delete=models.CASCADE)
    createdAt = models.DateTimeField("Created At", auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField("Updated At", auto_now_add=True, null=True, blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.typeName

    class Meta:
        db_table = "game"

class LeagueUserType(models.Model):
    typeName = models.CharField("name of user type", "name", max_length=255)
    createdAt = models.DateTimeField("Created At", auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField("Updated At", auto_now_add=True, null=True, blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.typeName

    class Meta:
        db_table = "league_user_type"

class LeagueUser(models.Model):
    name = models.CharField("name of user", "name", max_length=255)
    email = models.EmailField(blank = True, null = True)
    height = models.FloatField("Height", blank=True, null=True)
    userType = models.ForeignKey(LeagueUserType, related_name="user_type_id", on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name="team_id", on_delete=models.CASCADE, null=True)
    isLoggedIn = models.BooleanField("is user logged in", default=False)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField("Updated At", auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "league_user"
