from django.shortcuts import render
from django.db.models import Sum

from .models import Fund, Match, Match_player, Match_venue, Player, Team

def index(request):
    return render(request, 'home.html')

def players(request):
    players = Player.objects.all()
    context = {'players' : players}
    return render(request, 'players.html', context)

def teams(request):
    teams = Team.objects.all()
    context = {'teams' : teams}
    return render(request, 'teams.html', context)

def grounds(request):
    grounds = Match_venue.objects.all()
    context = {'grounds' : grounds}
    return render(request, 'grounds.html', context)

def matches(request):
    matches = Match.objects.all()
    context = {'matches' : matches}
    return render(request, 'matches.html', context)

def match(request,pk):
    match = Match.objects.get(id=pk)
    match_players = Match_player.objects.filter(match=match)
    context = {
        'match' : match,
        'match_players' : match_players,
    }
    return render(request, 'match.html', context)

def funds(request):
    funds = Player.objects.annotate(payable = Sum('fund__amount') - Sum('fund__amount_paid'))
    context = {
        'funds':funds
    }
    return render(request, 'funds.html' , context)