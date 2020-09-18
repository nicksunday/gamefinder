from django.shortcuts import render, get_object_or_404
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

def game_selection_view(request):
    if request.method == 'POST':
        form = GameSelectionForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            print(category.category)
            return HttpResponseRedirect('/selection/')
    else:
        form = GameSelectionForm()

    return render(request, 'game_search.html', {'form': form})
