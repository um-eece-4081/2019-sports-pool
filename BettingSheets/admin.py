from django.contrib import admin

from .models import MasterBettingSheet

# Register your models here.
admin.site.register(MasterBettingSheet)
admin.site.site_header = 'Manage Betting Sheets'
