from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.models import User
import json
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class LandingView(TemplateView):
    template_name = 'user/landing.html'


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'user/login.html')


class LoginValidation(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('index')
        else:
            JsonResponse({'su': True})
            return redirect('login')


class RegisterView(TemplateView):
    template_name = 'user/register.html'


class IndexView(TemplateView, LoginRequiredMixin):
    template_name = 'user/base.html'
