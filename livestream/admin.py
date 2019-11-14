from django.contrib import admin

from .models import Users, BotAction, Coordinates
# Register your models here.

admin.site.register(Users)
admin.site.register(BotAction)
admin.site.register(Coordinates)
