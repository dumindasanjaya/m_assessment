from django.contrib import admin
from django.urls import path
from league_stats_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'league_user', views.LeagueUserAPIView.as_view(), name='league-user-list'),
    path(r'team', views.TeamAPIView.as_view(), name='team-list'),
    path(r'game', views.GameAPIView.as_view(), name='game-list'),
]
