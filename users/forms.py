from django import forms
from django.contrib.auth.models import User
import re

class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
        label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Validate minimum 8 characters
        if len(username) < 8:
            raise forms.ValidationError("Username must be at least 8 characters long.")

        # Validate at least one number
        if not re.search(r'\d', username):
            raise forms.ValidationError("Username must contain at least one number.")

        # Validate at least one symbol
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', username):
            raise forms.ValidationError("Username must contain at least one special character.")

        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data

