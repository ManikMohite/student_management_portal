from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "roll_no",
            "department",
            "semester",
            "phone",
            "address",
            "photo"
        ]

        widgets = {

            "roll_no": forms.TextInput(attrs={"class":"form-control"}),

            "department": forms.TextInput(attrs={"class":"form-control"}),

            "semester": forms.NumberInput(attrs={"class":"form-control"}),

            "phone": forms.TextInput(attrs={"class":"form-control"}),

            "address": forms.Textarea(attrs={"class":"form-control"}),

            "photo": forms.FileInput(attrs={"class":"form-control"}),

        }