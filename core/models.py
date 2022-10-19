from django.db import models

class Match_venue(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Match(models.Model):
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey(Match_venue, null=True, on_delete=models.SET_NULL)
    fee = models.IntegerField()
    target_score = models.IntegerField()
    chase_score = models.IntegerField()

    def __str__(self):
        return str(self.venue) + str("-") + str(self.date)

class Match_player(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    player_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_batting_score = models.IntegerField(null=True)
    player_bowling_score = models.IntegerField(null=True)
    player_over = models.IntegerField(null=True)

    def __str__(self):
        return str(self.player_team) + str("-") + str(self.player)

class Fund(models.Model):
    date = models.DateField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    amount = models.IntegerField()
    amount_paid = models.IntegerField()

    def __str__(self):
        return str(self.player.name) + ' - ' + str(self.amount_paid) + '/' + str(self.amount)