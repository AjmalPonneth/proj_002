from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import login as dj_login
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import NewUser
from django.http import HttpResponse
from twilio.rest import Client
from django.contrib.auth.hashers import make_password
from decouple import config
from django.conf import settings
from django.views.generic.detail import DetailView
from .models import UserSkills
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
        user_skills = data['user_skills']
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

        # Skills

        if user_skills:
            if len(user_skills) == 10:
                UserSkills.objects.create(
                    user=self.request.user, python=True, javascript=True, php=True, java=True, cpp=True, csharp=True, ruby=True, go=True, r=True)
            else:
                skill = UserSkills(user=self.request.user)
                if 'python' in user_skills:
                    skill.python = True
                if 'javascript' in user_skills:
                    skill.javascript = True
                if 'php' in user_skills:
                    skill.php = True
                if 'java' in user_skills:
                    skill.java = True
                if 'cpp' in user_skills:
                    skill.cpp = True
                if 'ruby' in user_skills:
                    skill.ruby = True
                if 'go' in user_skills:
                    skill.go = True
                if 'r' in user_skills:
                    skill.r = True
                skill.save()
        # User goal
        if user_goal:
            NewUser.objects.filter(email=request.user).update(goal=user_goal)
        # User best thing about coding
        if user_best:
            NewUser.objects.filter(email=request.user).update(
                best_thing=user_best)
        # User current project
        if user_current_project:
            NewUser.objects.filter(email=request.user).update(
                current_project=user_current_project)
        # User fav language
        if user_fav_lang:
            NewUser.objects.filter(email=request.user).update(
                fav_language=user_fav_lang)
        return JsonResponse({'success': True}, safe=False)


class EachUserProfile(LoginRequiredMixin, DetailView):
    model = NewUser


class LogoutView(View):
    url = 'login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect(self.url)

    def post(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect(self.url)
