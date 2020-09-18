from django import forms
from .models import Categories

class GameSelectionForm(forms.Form):
    #category_dict = {}
    #for c in Categories.objects.all():
    #    category_dict[c.category_id] = c.category
    categories = Categories.objects.all()
    testName = forms.CharField(max_length=100, label='Test name', required=False)
    category = forms.ModelMultipleChoiceField(label='Select a category', required=False,
            queryset=categories, to_field_name="category")
            #widget=forms.Select(choices = Categories.objects.all()))#category_dict.items()))
