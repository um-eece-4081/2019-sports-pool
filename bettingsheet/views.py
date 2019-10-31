from django.shortcuts import render
from django.http import HttpResponse

from bettingsheet.models import Game
from bettingsheet.models import MasterBettingSheet
from .forms import GameModelChoiceField


# Create your views here.
def contact(request):
    games = Game.objects.all;
    if request.method == 'POST':
        form = GameModelChoiceField(request.POST)
    form = GameModelChoiceField()
    return render(request, 'forms.html', {'games': games})
