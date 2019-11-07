from django.db import models, transaction
from django.contrib import admin
# Create your models here.




class Game(models.Model):
    game_of_the_week = models.BooleanField(default=False)
    betting_sheet = models.ForeignKey('MasterBettingSheet', on_delete=models.CASCADE, null=True,
                                      verbose_name='Master Betting Sheet')
    favorite_team = models.CharField(max_length=20, null=True, blank=False,
                                     verbose_name='Favorite Team')
    underdog_team = models.CharField(max_length=20, null=True, blank=False, verbose_name='Underdog Team')
    favorite_score = models.PositiveIntegerField(null=True, blank=False, default=None)
    betting_line = models.PositiveIntegerField(null=True, blank=False, default=None)
    underdog_score = models.PositiveIntegerField(null=True, blank=False, default=None)
    network_name = models.CharField(max_length=10, null=True, blank=False)
    date_time = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.game_of_the_week:
            return super(Game, self).save(*args, **kwargs)
        with transaction.atomic():
            Game.objects.filter(game_of_the_week=True).update(game_of_the_week=False)
            return super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.favorite_team) + " VS " + str(self.underdog_team)

    def winner(self):
        if favorite_score > (underdog_score + betting_line):
            return favorite_team
        else:
            return underdog_team


class MasterBettingSheet(models.Model):
    is_published = models.BooleanField(editable=False, max_length=10, default='False')
    is_scored = models.BooleanField(editable=False, null=False, blank=False, default=False)
    title = models.CharField(max_length=30, editable=True, blank=False, null=False,
                             default="Week of MM/DD-MM/DD")

    def __str__(self):
        return str(self.title)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_of_the_week = ""


class UserGameSelection(models.Model):
    game = models.OneToOneField(
           Game,
           on_delete = models.CASCADE,
           primary_key = True
           )
    high_risk = models.BooleanField(editable=False, max_length=10, default='False')
    selected_team = models.CharField(max_length=30, editable=True, blank=False, null=False)
    game_of_the_week_score = models.SmallIntegerField()


    #-----------------------
    #------- TEAM4 ---------
    #-----------------------

    def score(self):
        if self.selected_team == self.game.winner(): #winner() function will reside in Game
           return 1
        else:
           return 0

    def winston_score(self):
        if self.selected_team == self.game.winner(): #winner() function will reside in Game
           return 1
        elif self.selected_team == self.game.winner():
            pass
        else:
           return 0

class Bettor(models.Model):
    #def __init__(self, is_winston_cup, betting_sheet, weekly_points, winston_points, user_id):
    is_winston_cup = models.BooleanField(default=False)
    betting_sheet = models.ForeignKey('MasterBettingSheet', on_delete=models.CASCADE, null=True, verbose_name='Master Betting Sheet')
    weekly_points = models.PositiveIntegerField(null=True, blank=False, default=None)
    winston_points = models.PositiveIntegerField(null=True, blank=False, default=None)
    currentPoints = models.PositiveIntegerField(null=True, blank=False, default=None)

    def score_week(self, wk):
        sheet = UserSheet.objects.filter(bettor = self, week = wk)
        score = 0
        for game in sheet.UserGameSelection_set.all():
            score = score + game.score()
        weekly_points = score
        

    def score_winston(self):
        pass

class Ranking(models.Model):
    title = models.CharField(max_length=30, editable=True, blank=False, null=False, default="Week of MM/DD-MM/DD")
    
    def __str__(self):
        return self.title
    
    bettor = models.ManyToManyField(
           Bettor,
           on_delete = models.CASCADE,
           primary_key = True
           )
    def rank():
        pass
        
            
        
        
