from django.db import models

class User(models.Model):
    #def __init__(self, is_winston_cup, betting_sheet, weekly_points, winston_points, user_id):
    is_winston_cup = models.BooleanField(default=False)
    betting_sheet = models.ForeignKey('MasterBettingSheet', on_delete=models.CASCADE, null=True, verbose_name='Master Betting Sheet')
    weekly_points = models.PositiveIntegerField(null=True, blank=False, default=None)
    winston_points = models.PositiveIntegerField(null=True, blank=False, default=None)
    user_id = models.PositiveIntegerField(null=True, blank=False, default=None)
    currentPoints = models.PositiveIntegerField(null=True, blank=False, default=None)
    def get_is_winston_cup(self):
        return self.is_winston_cup
    def get_betting_sheet(self):
        return self.betting_sheet
    def get_weekly_points(self):
        return self.weekly_points
    def get_winston_points(self):
        return self.winston_points
    def set_weekly_points(self, we_points):
        self.weekly_points = w_points
    def set_winston_points(self, wi_points):
        self.winston_points = wi_points
    def get_user_id(self):
        return self.user_id

for user in list:
    user.get_weekly_points
