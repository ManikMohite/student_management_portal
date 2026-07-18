from django import forms
from django.contrib.auth.models import User
from students.models import Student


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )

   

class StudentRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    roll_no = forms.CharField(max_length=20)
    department = forms.CharField(max_length=100)
    semester = forms.IntegerField()
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)