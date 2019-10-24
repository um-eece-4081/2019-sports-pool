from django.db import models
from django.http import HttpRequest


# Create your models here.
class Game(models.Model):
    team1 = models.TextField(max_length=4, null=True, blank=False)
    team2 = models.TextField(max_length=4, null=True, blank=False)
    betting_line = models.IntegerField(null=False, blank=False, default=-1)
    network_name = models.TextField(max_length=10, null=True, blank=False)
    date_time = models.TextField(max_length=30, null=True, blank=False)
    favorite_score = ""
    underdog_score = ""

    def set_score(self, score_pair):
        self.favorite_score = score_pair[0]
        self.underdog_score = score_pair[1]

    def edit_game_info(self):
        self.team1 = models.TextField(max_length=4, null=False, blank=False, default=self.team1)
        self.team2 = models.TextField(max_length=4, null=False, blank=False, default=self.team2)
        self.betting_line = models.IntegerField(null=False, blank=False, default=self.betting_line)
        self.network_name = models.TextField(max_length=10, null=False, blank=False, default=self.network_name)
        self.date_time = models.TextField(max_length=30, null=False, blank=False, default=self.date_time)


class MasterBettingSheet(models.Model):
    title = models.TextField(blank=False, null=False, default="Week of MM/DD-MM/DD")
    game_list = []
    is_published = False
    is_scored = False
    game_of_the_week = ""

    def score_games(self, score_pair_list):
        self.is_scored = True
        for_counter = 0
        for game in self.game_list:
            game.set_score(score_pair_list[for_counter])
            for_counter = for_counter+1

    def publish(self):
        self.is_published = True

    def set_game_of_the_week(self, game_number):
        self.game_of_the_week = game_number

    def edit_sheet(self):
        for game in self:
            game.edit_game_info()
