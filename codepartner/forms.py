from django import forms
from .models import Session


class SessionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date'
    }))
    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time'
    }))

    class Meta:
        model = Session
        fields = ('goal', 'language', 'level', 'desc', 'date', 'time')
