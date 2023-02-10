from django.forms import ModelForm
from django import forms
from .models import EditProjects, Cars

class EditProjectsForm(ModelForm):
    class Meta:
        model = EditProjects
        fields = ("date",)


class CarForm(forms.ModelForm):
    photo = forms.ImageField()
    
    class Meta:
        model = Cars
        fields = ['name', 'brand', 'trim', 'date', 'description', 'photo']