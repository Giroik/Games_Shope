from django.shortcuts import render
from django.views.generic import ListView, DetailView
from reviews.models import Game
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class GameListView(ListView):
    model=Game
    template_name="reviews/game_list.html"
    context_object_name="game_list"


class GameDetailViews(LoginRequiredMixin,DetailView):
    model=Game
    context_object_name="game"







#попробывать сделать функцию самостоятельно в место класса GameDetailViews


def home(request):
    return render(request,"Main.html")