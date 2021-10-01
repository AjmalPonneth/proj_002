from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import LandingView, LoginView, RegisterView, IndexView, LogoutView, OTPLoginView, OTPVerificationView, OTPVerfied, RegisterOTP
from django.contrib.auth import views as auth_views
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
    path('reset_password', auth_views.PasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
    ), name='password_reset_complete'),
]
