from django.shortcuts import render
from .models import Player, Ground, Booking, Expense

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
    if request.method == 'GET':
        bookings = Booking.objects.all()
        context = {'bookings' : bookings}
        return render(request, 'bookings.html', context)
    elif request.method == 'POST':
        ground = Ground.objects.get(id=request.POST.get('ground_id'))
        Booking.objects.create(
            date = request.POST.get('date'),
            ground = ground,
            amount = request.POST.get('fee'),
        )
        bookings = Booking.objects.all()
        context = {'bookings' : bookings}
        return render(request, 'bookings.html', context)

def add_booking(request):
    return render(request, 'add_booking.html')

def expenses(request):
    if request.method == 'GET':
        expenses = Expense.objects.all()
        context = {'expenses' : expenses}
        return render(request, 'expenses.html', context)
    elif request.method == 'POST':
        Expense.objects.create(
            date = request.POST.get('date'),
            name = request.POST.get('name'),
            amount = request.POST.get('amount'),
        )
        expenses = Expense.objects.all()
        context = {'expenses' : expenses}
        return render(request, 'expenses.html', context)

def add_expense(request):
    return render(request, 'add_expense.html')