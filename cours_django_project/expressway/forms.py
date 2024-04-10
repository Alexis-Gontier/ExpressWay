from django import forms
from expressway.models import Trains

# FORMULAIRE D'AJOUT DE TRAIN
class TrainsForm(forms.ModelForm):
    class Meta:
        model = Trains
        fields = [
            'trainID',
            'type',
            'n',
            'heure',
            'destination',
            'voie'
        ]
