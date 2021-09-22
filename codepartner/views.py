from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.models import User
import json
# Create your views here.


class LandingView(TemplateView):
    template_name = 'landing.html'


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'login.html')


class LoginValidation(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return JsonResponse({'valid': True})


class RegisterView(TemplateView):
    template_name = 'register.html'


class IndexView(TemplateView, View):
    template_name = 'base.html'
