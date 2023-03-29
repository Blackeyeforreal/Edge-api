from django.contrib import admin
from .models import CricketPlayer, CricketTeam, Users
# Register your models here.
admin.site.register(CricketPlayer)
admin.site.register(CricketTeam)
admin.site.register(Users)