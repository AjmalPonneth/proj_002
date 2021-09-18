from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
# Create your views here.


class LandingView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'
