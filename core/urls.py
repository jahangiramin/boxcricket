from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('players/', views.players, name='players'),
    path('matches/', views.matches, name='matches'),
    path('grounds/', views.grounds, name='grounds'),
    path('teams/', views.teams, name='teams'),
    path('matches/<int:pk>/',views.match, name='match'),
    path('funds/', views.funds, name='funds'),
]
