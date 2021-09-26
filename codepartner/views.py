from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import NewUser
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
        if self.request.user.is_authenticated:
            return redirect('index')
        return render(self.request, 'user/register.html')

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        username = data['username']
        email = data['email']
        phone = data['phone']
        password = data['password']
        if NewUser.objects.filter(user_name=username).exists():
            return JsonResponse({'usesr_name_exists': True})
        elif NewUser.objects.filter(email=email).exists():
            return JsonResponse({'email_exists': True})
        elif NewUser.objects.filter(phone_number=phone).exists():
            return JsonResponse({'phone_exists': True})
        else:
            NewUser.objects.create(
                user_name=username, email=email, phone_number=phone, password=password)
        return JsonResponse({'success': True})


class IndexView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'user/index.html')


class LogoutView(View):
    url = 'login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect(self.url)

    def post(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect(self.url)
