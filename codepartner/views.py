from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as dj_login
# Create your views here.


class LandingView(TemplateView):
    template_name = 'landing.html'


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'login.html')

    def post(self, request, *args, **kwargs):
        name = self.request.POST['username']
        print(name)
        password = self.request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Not Valid!')


class RegisterView(TemplateView):
    template_name = 'register.html'


class IndexView(TemplateView, View):
    template_name = 'index.html'
