from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from string import punctuation

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','password1','password2']

    
        def clean(self):
            cleaned_data = super().clean()
            username = self.cleaned_data['username']
            if username.startswith('abc') or username.startswith('ABC') or (username.isdigit())or len(username)<4 or (username.startswith(punctuation)):
                raise forms.ValidationError('Invalid Username')