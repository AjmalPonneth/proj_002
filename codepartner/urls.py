from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import LandingView, LoginView, RegisterView, IndexView
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('login', csrf_exempt(
        LoginView.as_view()
    ), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('index', IndexView.as_view(), name='index'),

]
