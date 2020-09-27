from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.views import generic
from .forms import GameSelectionForm
from .models import *

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
                SearchedTerms.objects.create(term=artist.name)
                games = games.filter(artists__name=artist.name)
            if designer:
                SearchedTerms.objects.create(term=designer.designer)
                games = games.filter(designers__designer=designer.designer)
            if publisher:
                SearchedTerms.objects.create(term=publisher.publisher)
                games = games.filter(publishers__publisher=publisher.publisher)
            if categories:
                for category in categories:
                    SearchedTerms.objects.create(term=category.category)
                games = games.filter(categories__in=categories)
            if families:
                for family in families:
                    SearchedTerms.objects.create(term=family.family)
                games = games.filter(families__in=families)
            if mechanics:
                for mechanic in mechanics:
                    SearchedTerms.objects.create(term=mechanic.mechanic)
                games = games.filter(mechanics__in=mechanics)
            if subdomains:
                for subdomain in subdomains:
                    SearchedTerms.objects.create(term=subdomain.subdomain)
                games = games.filter(subdomains__in=subdomains)

            if min_player_count and max_player_count:
                min_str = f'{min_player_count} Player Games'
                max_str = f'{max_player_count} Player Games'
                SearchedTerms.objects.create(term=min_str)
                SearchedTerms.objects.create(term=max_str)
                if max_player_count < min_player_count:
                    games = games.filter(Q(minplayers__lte=max_player_count) & Q(maxplayers__gte=min_player_count))
                else:
                    games = games.filter(Q(minplayers__lte=min_player_count) & Q(maxplayers__gte=max_player_count))
            elif min_player_count:
                min_str = f'{min_player_count} Player Games'
                SearchedTerms.objects.create(term=min_str)
                games = games.filter(Q(minplayers__lte=min_player_count) & Q(maxplayers__gte=min_player_count))
            elif max_player_count:
                max_str = f'{max_player_count} Player Games'
                SearchedTerms.objects.create(term=max_str)
                games = games.filter(maxplayers__gte=max_player_count)

            if games:
                for game in games[:5]:
                    SuggestedGames.objects.create(game_id=game.game_id)
                    for mechanic in game.mechanics.all():
                        PopularMechanics.objects.create(mechanic=mechanic.mechanic)

            request.session['__selection_data'] = list(games.order_by('game_id').values().distinct()[:5])

            return redirect('game_selection_view')
    else:
        form = GameSelectionForm()

    return render(request, 'game_search.html', {'form': form})

def game_selection_view(request):
    return render(request, 'game_selection.html', {'games': request.session['__selection_data']})

def data_visualization_view(request):
    return render(request, 'data_visualization.html')
