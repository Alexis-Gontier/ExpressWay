from django import forms
from expressway.models import Trains

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
