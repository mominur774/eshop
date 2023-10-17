from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import CreateView
from accounts.models import User
from accounts.forms import RegistrationForm, LoginForm

# Create your views here.


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


class RegistrationView(CreateView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm
    success_url = '/accounts/login'


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))