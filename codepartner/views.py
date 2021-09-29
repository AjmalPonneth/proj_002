from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import NewUser
from django.http import HttpResponse
from twilio.rest import Client
from django.contrib.auth.hashers import make_password
from decouple import config
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
            NewUser.objects.create(
                username=username, email=email, phone_number=num, password=make_password(password))
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
        num = self.request.POST['phone']
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
        account_sid = config('ACCOUNT_SID', cast=str)
        auth_token = config('AUTH_TOKEN', cast=str)
        service_id = config('SERVICE_ID')
        print(service_id)
        client = Client(account_sid, auth_token)
        verification_check = client.verify \
            .services(service_id) \
            .verification_checks \
            .create(to='+91'+num, code=otp)
        if verification_check.status == 'approved':
            user = NewUser.objects.filter(phone_number=num)
            auth.authenticate(request, username=user.email,
                              password=user.password)
            auth.login(request, user,
                       backend='djago.contrib.auth.backends.ModelBackend')
            return redirect('index')
        messages.info(request, 'Your otp is not valid')
        return redirect('verified')


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
