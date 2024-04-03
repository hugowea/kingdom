from django import forms
from app.models import Kingdom

class SubordinateForm(forms.Form):
    name = forms.CharField(label="Имя:", max_length=128)
    kingdom = forms.CharField(label="Королевство:")
    age = forms.IntegerField(label="Возраст:",)
    email = forms.CharField(label="Голубь (email):", max_length=128)
