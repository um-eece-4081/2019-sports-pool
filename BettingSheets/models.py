from django.db import models
from django.http import HttpRequest

# Create your models here.


class Game(models.Model):
    betting_sheet = models.ForeignKey('MasterBettingSheet', on_delete=models.CASCADE, null=True,
                                      verbose_name='Master Betting Sheet')
    favorite_team = models.TextField(max_length=4, null=True, blank=False,
                                     verbose_name='Favorite Team')
    underdog_team = models.TextField(max_length=4, null=True, blank=False,
                                     verbose_name='Underdog Team')
    betting_line = models.IntegerField(null=False, blank=False, default=-1)
    network_name = models.TextField(max_length=10, null=True, blank=False)
    date_time = models.DateTimeField(null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.favorite_score = ""
        self.underdog_score = ""

    def __str__(self):
        return self.favorite_team + " VS " + self.underdog_team

    def set_score(self, score_pair):
        self.favorite_score = score_pair[0]
        self.underdog_score = score_pair[1]


class MasterBettingSheet(models.Model):
    title = models.TextField(blank=False, null=False, default="Week of MM/DD-MM/DD")

    def __str__(self):
        return str(self.title)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_published = False
        self.is_scored = False
        self.game_of_the_week = ""

    def publish(self):
        self.is_published = True
