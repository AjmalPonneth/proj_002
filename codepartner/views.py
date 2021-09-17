from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class LandingView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'
