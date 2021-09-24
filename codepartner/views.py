from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
import json
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class LandingView(TemplateView):
    template_name = 'user/landing.html'


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return render(self.request, 'user/login.html')

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        username = data['username']
        password = data['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({'success': True}, safe=False)
        else:
            return JsonResponse({'success': False}, safe=False)
        return JsonResponse(data)


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'user/register.html')

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        username = data['username']
        email = data['email']
        phone = data['phone']
        password = data['password']
        return JsonResponse(data)


class IndexView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'user/base.html')


class LogoutView(View):
    url = 'login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect(self.url)
