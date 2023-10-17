from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from accounts.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['required'] = True
            self.fields[field_name].widget.attrs['autofocus'] = False



class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=255, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }))
    password = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }))

