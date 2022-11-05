from django.shortcuts import render
from .models import Player, Ground, Booking, Expense, Booking_Player
from django.db.models import Sum


def index(request):
    return render(request, 'home.html')

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
            number = request.POST.get('number'),
            tagline = request.POST.get('tagline')
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
        ground = Ground.objects.get(id=request.POST.get('ground'))
        Booking.objects.create(
            date = request.POST.get('date'),
            ground = ground,
            amount = request.POST.get('amount'),
        )
        bookings = Booking.objects.all()
        context = {'bookings' : bookings}
        return render(request, 'bookings.html', context)

def add_booking(request):
    grounds = Ground.objects.all()
    context = {
        'grounds' : grounds
    }
    return render(request, 'add_booking.html', context)

def booking_players(request, pk):
    if request.method =='GET':
        booking = Booking.objects.get(id=pk)
        context = {
            'booking' : booking
        }

        return render(request, 'booking_players.html', context)
    elif request.method == 'POST':
        booking = Booking.objects.get(id = pk)
        player = Player.objects.get(id = request.POST.get('player'))
        Booking_Player.objects.create(
            booking = booking,
            player = player,
            amount = request.POST.get('amount'),
            fee_paid = request.POST.get('fee_paid')
        )
        booking = Booking.objects.get(id=pk)
        context = {
            'booking' : booking
        }
        return render(request, 'booking_players.html', context)

def add_booking_players(request, pk):
    booking = Booking.objects.get(id=pk)
    players = Player.objects.all()
    context = {
        'booking' : booking,
        'players' : players
    }
    return render(request, 'add_booking_players.html', context)

def expenses(request):
    if request.method == 'GET':
        expenses = Expense.objects.all()
        expense_sum = expenses.aggregate(Sum('amount'))
        print(expense_sum)
        context = {
            'expenses' : expenses,
            'expense_sum': expense_sum
        }
        return render(request, 'expenses.html', context)

    elif request.method == 'POST':
        Expense.objects.create(
            date = request.POST.get('date'),
            name = request.POST.get('name'),
            amount = min(request.POST.get('amount')),
        )
        expenses = Expense.objects.all()
        context = {'expenses' : expenses}
        return render(request, 'expenses.html', context)

def add_expense(request):
    return render(request, 'add_expense.html')

def funds(request):
    expenses = Expense.objects.all()    
    expenses_sum = expenses.aggregate(Sum('amount'))

    booking_fees = Booking.objects.all()
    booking_fees_sum = booking_fees.aggregate(Sum('amount'))

    player_contributions = Booking_Player.objects.filter(fee_paid='True')
    player_contributions_sum = player_contributions.aggregate(Sum('amount'))

    balance = player_contributions_sum['amount__sum'] - booking_fees_sum['amount__sum'] - expenses_sum['amount__sum']

    transactions = []

    for expense in expenses:
        expense.amount = expense.amount * -1
        transactions.append(expense)
    
    for booking_fee in booking_fees:
        booking_fee.amount = booking_fee.amount * -1
        transactions.append(booking_fee)

    for player_contribution in player_contributions:
        transactions.append(player_contribution)

    context = {
        'transactions' : transactions,
        'balance' : balance
    }

    return render(request, 'funds.html', context)