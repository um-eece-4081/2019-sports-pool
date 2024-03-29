from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager 


class Bettor(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    # This gets updated if doing the Winston Cup
    is_winston_user = models.BooleanField(default=False)
    # This gets updated if doing the weekly game
    paid_this_week = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BettorManager()

    def __str__(self):
        return self.get_full_name()

    def score_week(self, wk):
        sheet = UserSheet.objects.filter(bettor=self, week=wk)
        score = 0
        for game in sheet.user_game_selection_set.all():
            score = score + game.score()

        return score


    def score_winston(self):
        pass


class WeeklyScores(models.Model):
    bettor = models.ForeignKey('Bettor', on_delete=models.CASCADE, null=True, verbose_name='Bettor')
    score = models.PositiveSmallIntegerField()
    week = models.PositiveSmallIntegerField()

    def __str__(self):
        return "The score of week" + self.week + " for " + self.bettor + "is: " + self.score + " points."

class WinstonScores(models.Model):
    bettor = models.OneToOneField('Bettor', on_delete=models.CASCADE, null=True, verbose_name='Bettor')
    overall_score = models.SmallIntegerField()

    def __str__(self):
        return "The winston score for " + self.bettor + " is: " + self.overall_score + " points."
