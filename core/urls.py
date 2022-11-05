from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('grounds/', views.grounds, name='grounds'),
    path('add-ground/', views.add_ground, name='add_ground'),
    path('players/', views.players, name='players'),
    path('add-player', views.add_player, name='add_player'),
    path('bookings/', views.bookings, name='bookings'),
    path('add-booking/', views.add_booking, name='add_booking'),
    path('booking/<str:pk>', views.booking_players, name='booking_players'),
    path('booking/<str:pk>/add-booking-players', views.add_booking_players, name='add_booking_players'),
    path('expenses/', views.expenses, name='expenses'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('funds/', views.funds, name='funds'),
    path('pending-contributions', views.pending_contributions, name='pending_contributions'),
]
