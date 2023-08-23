from django import forms

class Registration(forms.Form):
    name = forms.CharField(max_length=50)
    Enrollment = forms.CharField(max_length=12)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)