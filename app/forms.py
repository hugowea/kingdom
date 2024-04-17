from django import forms
from app.models import Kingdom, Subordinate, King

class SubordinateForm(forms.ModelForm):
    kingdom = forms.ModelChoiceField(queryset=Kingdom.objects.all())
    class Meta:
        model = Subordinate 
        fields = ("name", "kingdom", "age", "email")

class KingForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=King.objects.all())
    class Meta:
        model = King 
        fields = ("name",)

class KingSubordinatesForm(forms.ModelForm):
    name = None
    def __init__(self, subordinates):
        global name
        self.subordinates = subordinates
        name = forms.ModelChoiceField(queryset=subordinates)
    class Meta:
        model = King 
        fields = ("name",)