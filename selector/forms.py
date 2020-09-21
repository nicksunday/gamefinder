from django import forms
from .models import *

class GameSelectionForm(forms.Form):
    all_categories = Categories.objects.all()
    categories = forms.ModelMultipleChoiceField(label='Select categories', required=False,
            queryset=all_categories)

    all_families = Families.objects.exclude(family__icontains='admin: ').exclude(family__icontains='game: ')
    families = forms.ModelMultipleChoiceField(label='Select themes', required=False,
            queryset=all_families)

    all_mechanics = Mechanics.objects.all()
    mechanics = forms.ModelMultipleChoiceField(label='Select game mechanics', required=False,
            queryset=all_mechanics)

    all_subdomains = Subdomains.objects.all()
    subdomains = forms.ModelMultipleChoiceField(label='Select subdomains', required=False,
            queryset=all_subdomains)

    minplayers = forms.IntegerField(label='Minimum Player Count', required=False, min_value=1, max_value=100)

    maxplayers = forms.IntegerField(label='Maximum Player Count', required=False, min_value=1, max_value=100)

    all_artists = Artists.objects.all()
    artists = forms.ModelChoiceField(label='Select an artist', required=False,
            queryset=all_artists)

    all_designers = Designers.objects.all()
    designers = forms.ModelChoiceField(label='Select a designer', required=False,
            queryset=all_designers)

    all_publishers = Publishers.objects.all()
    publishers = forms.ModelChoiceField(label='Select a publisher', required=False,
            queryset=all_publishers)
