from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import login as dj_login
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import NewUser
from twilio.rest import Client
from django.contrib.auth.hashers import make_password
from decouple import config
from django.conf import settings
from django.views.generic.detail import DetailView
from .models import UserSkills
from accounts.forms import ProfileImageForm
from django.views.generic.edit import FormView
from .forms import SessionForm
# Create your views here.


class LandingView(TemplateView):
    template_name = 'user/landing.html'


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return render(self.request, 'account/login.html')

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
        return render(self.request, 'account/signup.html')

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        username = data['username']
        email = data['email']
        phone = data['phone']
        password = data['password']
        self.request.session['phone'] = phone
        if NewUser.objects.filter(username=username).exists():
            return JsonResponse({'usesr_name_exists': True})
        elif NewUser.objects.filter(email=email).exists():
            return JsonResponse({'email_exists': True})
        elif NewUser.objects.filter(phone_number=phone).exists():
            return JsonResponse({'phone_exists': True})
        else:
            self.request.session['username'] = username
            self.request.session['email'] = email
            self.request.session['phone'] = phone
            self.request.session['password'] = password
            account_sid = config('ACCOUNT_SID')
            auth_token = config('AUTH_TOKEN')
            client = Client(account_sid, auth_token)
            verification = client.verify \
                .services(config('SERVICE_ID')) \
                .verifications \
                .create(to='+91'+phone, channel='sms')
        return JsonResponse({'success': True})


class RegisterOTP(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/otp_verify.html')

    def post(self, request, *args, **kwargs):
        username = self.request.session['username']
        email = self.request.session['email']
        num = self.request.session['phone']
        password = self.request.session['password']
        otp = self.request.POST['otp']
        account_sid = config('ACCOUNT_SID')
        auth_token = config('AUTH_TOKEN')
        client = Client(account_sid, auth_token)
        verification_check = client.verify \
            .services(config('SERVICE_ID')) \
            .verification_checks \
            .create(to='+91'+num, code=otp)
        if verification_check.status == 'approved':
            user = NewUser(
                username=username, email=email, phone_number=num, password=make_password(password))
            user.save()
            dj_login(request, user,
                     'django.contrib.auth.backends.ModelBackend')
            del username
            del email
            del num
            del password
            return redirect('login')
        messages.info(request, 'Your otp is not valid')
        return redirect('register_otp')


class OTPLoginView(TemplateView):
    template_name = 'user/otp_login.html'


class OTPVerificationView(View):
    def post(self, request, *args, **kwargs):
        num = self.request.POST['phone'].replace(" ", "")
        self.request.session['phone'] = num
        if NewUser.objects.filter(phone_number=num).exists():
            account_sid = config('ACCOUNT_SID')
            auth_token = config('AUTH_TOKEN')
            client = Client(account_sid, auth_token)
            verification = client.verify \
                .services(config('SERVICE_ID')) \
                .verifications \
                .create(to='+91'+num, channel='sms')
        else:
            messages.info(request, 'This phone number not exists!')
            return redirect('otp')
        return redirect('verified')


class OTPVerfied(OTPVerificationView):
    def get(self, request, *args, **kwargs):

        return render(request, 'user/otp_verify.html')

    def post(self, request, *args, **kwargs):
        num = self.request.session['phone']
        otp = self.request.POST['otp']
        account_sid = config('ACCOUNT_SID')
        auth_token = config('AUTH_TOKEN')
        service_id = config('SERVICE_ID')
        client = Client(account_sid, auth_token)
        verification_check = client.verify \
            .services(service_id) \
            .verification_checks \
            .create(to='+91'+num, code=otp)
        if verification_check.status == 'approved':
            user = NewUser.objects.get(phone_number=num)
            dj_login(
                request, user, backend='codepartner.backend.CaseSensitiveModelBackend')
            return redirect('index')
        messages.info(request, 'Your otp is not valid')
        return redirect('verified')


class IndexView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'user/index.html')


class ProfileView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'user/user_profile.html')

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        first_name = data.get('first_name')
        phone = data.get('phone')
        user_exp = data.get('user_exp')
        user_goal = data.get('user_goal')
        user_best = data.get('user_best')
        user_current_project = data.get('user_current_project')
        user_fav_lang = data.get('user_fav_lang')
        user_image = data.get('image')
        # Firstname
        if len(first_name) > 1:
            user = NewUser.objects.filter(
                email=self.request.user).update(first_name=first_name)
        # Phone
        if NewUser.objects.exclude(email=self.request.user).filter(phone_number=phone).exists():
            return JsonResponse({'phone_exists': True})
        else:
            NewUser.objects.filter(
                email=self.request.user).update(phone_number=phone)
        # User Exp
        if user_exp:
            NewUser.objects.filter(
                email=self.request.user).update(user_exp=user_exp)
        # User goal
        if user_goal:
            NewUser.objects.filter(
                email=self.request.user).update(goal=user_goal)
        # User best thing about coding
        if user_best:
            NewUser.objects.filter(email=self.request.user).update(
                best_thing=user_best)
        # User current project
        if user_current_project:
            NewUser.objects.filter(email=self.request.user).update(
                current_project=user_current_project)
        # User fav language
        if user_fav_lang:
            NewUser.objects.filter(email=self.request.user).update(
                fav_language=user_fav_lang)
        return JsonResponse({'success': True}, safe=False)


class CreateUserSkill(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        skills = data.get('skills')
        if "Python" in skills:
            UserSkills.objects.filter(user=self.request.user).update(
                python=True)
        else:
            UserSkills.objects.filter(user=self.request.user).update(
                python=False)
        if "Javascript" in skills:
            UserSkills.objects.filter(user=self.request.user).update(
                javascript=True)
        else:
            UserSkills.objects.filter(user=self.request.user).update(
                javascript=False)
        if "Java" in skills:
            UserSkills.objects.filter(user=self.request.user).update(
                java=True)
        else:
            UserSkills.objects.filter(user=self.request.user).update(
                java=False)
        if "C++" in skills:
            UserSkills.objects.filter(user=self.request.user).update(
                cpp=True)
        else:
            UserSkills.objects.filter(user=self.request.user).update(
                cpp=False)
        if "C#" in skills:
            UserSkills.objects.filter(user=self.request.user).update(
                csharp=True)
        else:
            UserSkills.objects.filter(user=self.request.user).update(
                csharp=False)
        if "PHP" in skills:
            UserSkills.objects.filter(user=self.request.user).update(
                php=True)
        else:
            UserSkills.objects.filter(user=self.request.user).update(
                php=False)
        if "Ruby" in skills:
            UserSkills.objects.filter(user=self.request.user).update(
                ruby=True)
        else:
            UserSkills.objects.filter(user=self.request.user).update(
                ruby=False)
        if "GO" in skills:
            UserSkills.objects.filter(user=self.request.user).update(
                go=True)
        else:
            UserSkills.objects.filter(user=self.request.user).update(
                go=False)
        if "R" in skills:
            UserSkills.objects.filter(user=self.request.user).update(
                r=True)
        else:
            UserSkills.objects.filter(user=self.request.user).update(
                r=False)
        return JsonResponse({'success': True})


class UserSkillsView(View):
    def get(self, request, *args, **kwargs):
        qs = UserSkills.objects.get(user=self.request.user)
        user_skills = []
        if qs.python:
            user_skills.append("Python")
        if qs.javascript:
            user_skills.append("Javascript")
        if qs.php:
            user_skills.append("PHP")
        if qs.java:
            user_skills.append("Java")
        if qs.cpp:
            user_skills.append("C++")
        if qs.csharp:
            user_skills.append("C#")
        if qs.ruby:
            user_skills.append("Ruby")
        if qs.go:
            user_skills.append("Go")
        if qs.r:
            user_skills.append("R")
        return JsonResponse({'skills': user_skills})


class EachUserProfile(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = NewUser


class SessionCreateView(FormView):
    template_name = 'user/session_create.html'
    form_class = SessionForm
    success_url = 'index'


class LogoutView(View):
    url = 'login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect(self.url)

    def post(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect(self.url)
