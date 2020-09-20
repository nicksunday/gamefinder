from django import forms
from .models import *
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Column, Field

class GameSelectionForm(forms.Form):
    all_artists = Artists.objects.all()
    artists = forms.ModelChoiceField(label='Select an artist', required=False,
            queryset=all_artists)

    all_designers = Designers.objects.all()
    designers = forms.ModelChoiceField(label='Select a designer', required=False,
            queryset=all_designers)

    all_publishers = Publishers.objects.all()
    publishers = forms.ModelChoiceField(label='Select a publisher', required=False,
            queryset=all_publishers)

    all_categories = Categories.objects.all()
    categories = forms.ModelMultipleChoiceField(label='Select a category', required=False,
            queryset=all_categories)

    all_families = Families.objects.exclude(family__icontains='admin:')
    families = forms.ModelMultipleChoiceField(label='Select families', required=False,
            queryset=all_families)

    all_mechanics = Mechanics.objects.all()
    mechanics = forms.ModelMultipleChoiceField(label='Select game mechanics', required=False,
            queryset=all_mechanics)

    all_subdomains = Subdomains.objects.all()
    subdomains = forms.ModelMultipleChoiceField(label='Select subdomains', required=False,
            queryset=all_subdomains)

    minplayers = forms.IntegerField(label='Minimum Player Count', required=False, min_value=1, max_value=100)

    maxplayers = forms.IntegerField(label='Maximum Player Count', required=False, min_value=1, max_value=100)

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.helper = FormHelper()
#        self.helper.form_class = 'form-horizontal'
#        self.helper.label_class = 'col-lg-2'
#        self.helper.field_class = 'col-lg-8'
#        self.helper.layout = Layout(
#                Column('artists', css_class='form-group'),
#                'designers',
#                'publishers',
#                'categories',
#                'families',
#                'mechanics',
#                'subdomains'
                #Column('artists', css_class='form-group col-md-10 mb-0'),
                #Row(
                #    Column('designers', css_class='form-group col-md-6 mb-0'),
                #    Column('publishers', css_class='form-group col-md-4 mb-0'),
                #    css_class='form-row'
                #),
                #Row(
                #    Column('categories', css_class='form-group col-md-4 mb-0'),
                #    Column('mechanics', css_class='form-group col-md-6 mb-0'),
                #    css_class='form-row'
                #),
                #Row(
                #    Column('families', css_class='form-group col-md-8 mb-0'),
                #    Column('subdomains', css_class='form-group col-md-2 mb-0'),
                #    css_class='form_row'
                #)
#        )
