from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
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
        """Usernames should be unique (case insensitive)."""
        username = self.cleaned_data.get('username')

        # if another user has the same username (case insensitive match)
        if User.objects.filter(username__iexact=username):
            raise forms.ValidationError(u'Usernames must be unique.')
        
        return username

    def clean_email(self):
        """Email addresses should be unique (case Insensitive)."""
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        # if another user has the same email (case insensitive match)
        if User.objects.filter(email__iexact=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        
        return email

    def clean_password2(self):
        """The two passwords should match."""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError(u'Password must not be empty.')

        if password1 != password2:
            raise ValidationError(u'Passwords do not match.')

        return password2

class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)