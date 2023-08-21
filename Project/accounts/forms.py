from django import forms 

class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    

class UserLogingForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()