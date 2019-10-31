from django.db import models

class User(models.Model):
    #def __init__(self, is_winston_cup, betting_sheet, weekly_points, winston_points, user_id):
    is_winston_cup = models.BooleanField(default=False)
    betting_sheet = models.ForeignKey('MasterBettingSheet', on_delete=models.CASCADE, null=True, verbose_name='Master Betting Sheet')
    weekly_points = models.PositiveIntegerField(null=True, blank=False, default=None)
    winston_points = models.PositiveIntegerField(null=True, blank=False, default=None)
    user_id = models.PositiveIntegerField(null=True, blank=False, default=None)
    currentPoints = models.PositiveIntegerField(null=True, blank=False, default=None)

for user in list:
    user.get_weekly_points
