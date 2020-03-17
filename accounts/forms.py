from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        """
        Usernames should be unique (case insensitive).
        """
        username = self.cleaned_data.get('username')

        # If another user has the same username (case insensitive match)
        # or if the username matches another user's email (as letting
        # users log in with username or email)
        if User.objects.filter(Q(username__iexact=username) | 
                               Q(email__iexact=username)):
            # raise a validation error
            raise forms.ValidationError('Usernames must be unique.')
        
        return username

    def clean_email(self):
        """
        Email addresses should be unique (case Insensitive).
        """
        email = self.cleaned_data.get('email')

        # If another user has the same email (case insensitive match)
        # or if the email matches another user's username (as letting
        # users log in with username or email)
        if User.objects.filter(Q(username__iexact=email) | 
                               Q(email__iexact=email)):
            # raise a validation error
            raise forms.ValidationError('Email addresses must be unique.')
        
        return email

    def clean_password2(self):
        """
        The two passwords should match.
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError('Password must not be empty.')

        if password1 != password2:
            raise ValidationError('Passwords do not match.')

        return password2

class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)