from django.contrib import admin
from core.models import Fund, Match_player, Match_venue, Player, Team, Match

admin.site.register(Match_venue)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Match_player)
admin.site.register(Fund)