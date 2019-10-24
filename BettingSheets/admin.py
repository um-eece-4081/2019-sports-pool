from django.contrib import admin

from .models import MasterBettingSheet
from .models import Game

# Register your models here.
admin.site.register(MasterBettingSheet)
admin.site.register(Game)
admin.site.site_header = 'Manage Betting Sheets'
