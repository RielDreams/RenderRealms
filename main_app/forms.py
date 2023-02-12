from django.forms import ModelForm
from django import forms
from .models import EditProjects, Cars, Environments, Characters

class EditProjectsForm(ModelForm):
    class Meta:
        model = EditProjects
        fields = ("date",)

class CarForm(forms.ModelForm):
    photo = forms.ImageField()
    
    class Meta:
        model = Cars
        fields = ['name', 'brand', 'trim', 'date', 'description', 'photo']

class EnvironmentForm(forms.ModelForm):
    photo = forms.ImageField()
    
    class Meta:
        model = Environments
        fields = ['name', 'date', 'description', 'photo']
        
class CharacterForm(forms.ModelForm):
    photo = forms.ImageField()
    
    class Meta:
        model = Characters
        fields = ['name', 'date', 'description', 'photo']