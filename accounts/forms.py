from .models import NewUser
from django import forms


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('image',)
