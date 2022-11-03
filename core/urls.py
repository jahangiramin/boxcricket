from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('grounds/', views.grounds, name='grounds'),
    path('add-ground/', views.add_ground, name='add_ground'),
    path('players/', views.players, name='players'),
    path('add-player', views.add_player, name='add_player'),
    path('bookings/', views.bookings, name='bookings'),
]
