from django import forms
from .models import Mark

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = "__all__"

        widgets = {
            "student": forms.Select(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "internal": forms.NumberInput(attrs={"class": "form-control"}),
            "external": forms.NumberInput(attrs={"class": "form-control"}),
        }