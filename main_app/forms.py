from django.forms import ModelForm 
from .models import EditProjects

class EditProjectsForm(ModelForm):
    class Meta:
        model = EditProjects
        fields = ("date",)
