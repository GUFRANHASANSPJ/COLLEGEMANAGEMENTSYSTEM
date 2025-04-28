from django import forms
from .models import Event, PlacementManagement

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date','participants']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class PlacementManagementForm(forms.ModelForm):
    class Meta:
        model = PlacementManagement
        fields = ['company_name', 'job_role', 'package', 'skills_required','participants']


