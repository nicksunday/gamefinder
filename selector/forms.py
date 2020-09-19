from django import forms
#from .models import Categories
from .models import *

class GameSelectionForm(forms.Form):
    all_artists = Artists.objects.all()
    artists = forms.ModelChoiceField(label='Select an artist', required=False,
            queryset=all_artists)

    all_categories = Categories.objects.all()
    categories = forms.ModelMultipleChoiceField(label='Select a category', required=False,
            queryset=all_categories)

    all_designers = Designers.objects.all()
    designers = forms.ModelChoiceField(label='Select a designer', required=False,
            queryset=all_designers)

    all_families = Families.objects.exclude(family__icontains='admin:')
    families = forms.ModelMultipleChoiceField(label='Select families', required=False,
            queryset=all_families)

    all_mechanics = Mechanics.objects.all()
    mechanics = forms.ModelMultipleChoiceField(label='Select game mechanics', required=False,
            queryset=all_mechanics)

    all_publishers = Mechanics.objects.all()
    publishers = forms.ModelChoiceField(label='Select a publisher', required=False,
            queryset=all_publishers)

    all_subdomains = Subdomains.objects.all()
    subdomains = forms.ModelMultipleChoiceField(label='Select subdomains', required=False,
            queryset=all_subdomains)
