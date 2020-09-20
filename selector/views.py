from django.db.models import Q
from django.shortcuts import render, redirect, reverse
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
            artist = form.cleaned_data['artists']
            designer = form.cleaned_data['designers']
            publisher = form.cleaned_data['publishers']
            categories = form.cleaned_data['categories']
            families = form.cleaned_data['families']
            mechanics = form.cleaned_data['mechanics']
            subdomains = form.cleaned_data['subdomains']
            min_player_count = form.cleaned_data['minplayers']
            max_player_count = form.cleaned_data['maxplayers']

            games = Games.objects.all()
            if artist:
                games = games.filter(artists__name=artist.name)
            if designer:
                games = games.filter(designers__designer=designer.designer)
            if publisher:
                games = games.filter(publishers__publisher=publisher.publisher)
            if categories:
                games = games.filter(categories__in=categories)
            if families:
                games = games.filter(families__in=families)
            if mechanics:
                games = games.filter(mechanics__in=mechanics)
            if subdomains:
                games = games.filter(subdomains__in=subdomains)

            if min_player_count and max_player_count:
                if max_player_count < min_player_count:
                    ValidationError(_('Min Players is more than Max Players'))
                else:
                    games = games.filter(Q(minplayers=min_player_count) & Q(maxplayers=max_player_count))
            elif min_player_count:
                games = games.filter(minplayers=min_player_count)
            elif max_player_count:
                games = games.filter(maxplayers=max_player_count)


            request.session['__selection_data'] = list(games.order_by('game_id').values()[:5])

            # print(f'{len(categories)} categories')
            # for i in categories: print(f'{i.category}')
            # request.session['__selection_data'] = list(categories.values())
            
            return redirect('game_selection_view')
    else:
        form = GameSelectionForm()

    return render(request, 'game_search.html', {'form': form})

def game_selection_view(request):
    return render(request, 'game_selection.html', {'games': request.session['__selection_data']})
