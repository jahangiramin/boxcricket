from django.contrib import admin
from core.models import Ground, Player, Booking, Booking_Player, Expense

admin.site.register(Ground)
admin.site.register(Player)
admin.site.register(Booking)
admin.site.register(Booking_Player)
admin.site.register(Expense)