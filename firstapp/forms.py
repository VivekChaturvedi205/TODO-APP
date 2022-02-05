from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["Task_tittle","Task_details"]
        widgets = {
            "Task_tittle": forms.TextInput(attrs={"class": "form-control"}),
            "Task_details": forms.TextInput(attrs={"class": "form-control"}),
        }

