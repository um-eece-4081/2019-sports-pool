from django.db import models
from BettingSheets import models as betting_sheet_models
# Create your models here.

class CommonData(models.Model):
    username = models.CharField(max_length=25, null=True, blank=False, verbose_name='Username')
    user_id = models.PositiveSmallIntegerField(max_length=75, null=True, blank=False, verbose_name='User ID')

    class Meta:
        abstract=True



class WeeklyScores(CommonData):
    weekly_score = models.PositiveSmallIntegerField()

class WinstonScores(CommonData):
    weekly_score = models.SmallIntegerField()

class PastUserBettingSheets(CommonData):
    betting_sheet_id = models.Field
