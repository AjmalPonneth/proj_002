from django import forms
from .models import Session


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('goal', 'language', 'level', 'desc', 'date', 'time')
