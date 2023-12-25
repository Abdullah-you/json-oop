from django import forms
from .models import Tasks

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description']