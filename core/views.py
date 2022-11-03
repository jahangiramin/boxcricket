from django.shortcuts import render
from .models import Player, Ground, Booking

def index(request):
    return render(request, 'main.html')

def grounds(request):
    if request.method == 'GET':
        grounds = Ground.objects.all()
        context = {'grounds' : grounds}
        return render(request, 'grounds.html', context)

    elif request.method == "POST":
        Ground.objects.create(
            name = request.POST.get('name'),
            address = request.POST.get('address')
        )
        grounds = Ground.objects.all()
        context = {'grounds' : grounds}
        return render(request, 'grounds.html', context)


def add_ground(request):
    return render(request, 'add_ground.html')

def players(request):
    if request.method == 'GET':
        players = Player.objects.all()
        context = {'players' : players}
        return render(request, 'players.html', context)

    elif request.method == 'POST':
        Player.objects.create(
            name = request.POST.get('name'),
            number = request.POST.get('number')
        )
        players = Player.objects.all()
        context = {'players' : players}
        return render(request, 'players.html', context)

def add_player(request):
    return render(request, 'add_player.html')

def bookings(request):
    bookings = Booking.objects.all()
    context = {'booking' : booking}
    return render(request, 'booking.html', context)