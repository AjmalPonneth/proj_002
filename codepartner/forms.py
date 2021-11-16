from django import forms
from .models import Session, Comment


class SessionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'datepicker',
    }))
    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time',
        'class': 'timepicker',

    }))

    class Meta:
        model = Session
        fields = ('goal', 'language', 'level', 'desc', 'date', 'time')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
