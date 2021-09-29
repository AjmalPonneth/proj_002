from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import LandingView, LoginView, RegisterView, IndexView, LogoutView, OTPLoginView, OTPVerificationView, OTPVerfied, RegisterOTP
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('login', csrf_exempt(
        LoginView.as_view()
    ), name='login'),
    path('register', csrf_exempt(RegisterView.as_view()), name='register'),
    path('otp_login', OTPLoginView.as_view(), name="otp"),
    path('otp_register', RegisterOTP.as_view(), name="register_otp"),
    path('verification', OTPVerificationView.as_view(), name="otp_ver"),
    path('enter_otp', OTPVerfied.as_view(), name="verified"),
    path('index', IndexView.as_view(), name='index'),
    path('logout', LogoutView.as_view(), name='logout'),
]
