from django.shortcuts import render, redirect
#from django.http import HttpResponseRedirect
from django.views import generic
from .models import Artists, Categories, Designers, Families, GameArtists, GameCategories, GameDesigners, GameFamilies, GameMechanics, GamePublishers, GameSubdomains, Games, Mechanics, Publishers, Subdomains
from .forms import GameSelectionForm

# Create your views here.
def index(request):
    """View function for home page"""

    num_games = Games.objects.all().count()

    context = {
            'num_games': num_games,
    }

    return render(request, 'index.html', context=context)

class GamesListView(generic.ListView):
    model = Games
    paginate_by = 25

class GamesDetailView(generic.DetailView):
    model = Games

def game_search_view(request):
    if request.method == 'POST':
        form = GameSelectionForm(request.POST)
        if form.is_valid():
            categories = form.cleaned_data['categories']
            print(f'{len(categories)} categories')
            for i in categories: print(f'{i.category}')
            return redirect('/selector/search/', categories)
    else:
        form = GameSelectionForm()

    return render(request, 'game_search.html', {'form': form})
