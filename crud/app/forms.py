from django import forms
from .models import Project, Task



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description':  forms.Textarea(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'form-control'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'deadline', 'status']
        widgets = {
            'project': forms.Select(attrs={'class':'form-control'}),
            'title':  forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'type': 'form-control'}),
            'status': forms.Select(choices=Task.STATUS_CHOICES,attrs={'type': 'form-control'}),
        }