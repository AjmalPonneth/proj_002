from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import LandingView, LoginView, RegisterView, IndexView, LogoutView, OTPLoginView, OTPVerificationView, OTPVerfied, RegisterOTP, ProfileView, EachUserProfile, UserSkillsView, CreateUserSkill, SessionCreateView, SessionDetailView
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
    path('profile/<pk>', EachUserProfile.as_view(
        template_name='user/each_profile.html')),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'
                                                                                 ), name='password_reset_complete'),
    path('user_profile', csrf_exempt(ProfileView.as_view()), name='user_profile'),
    path('user_skills', UserSkillsView.as_view(), name='skills_view'),
    path('create_skills', csrf_exempt(
        CreateUserSkill.as_view()), name='create_skills'),
    path('session_create', SessionCreateView.as_view(), name="session_create"),
    path('session_detail/<pk>', SessionDetailView.as_view(
        template_name='user/session_detail.html'), name="session_detail"),
]
