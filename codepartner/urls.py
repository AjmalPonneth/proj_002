from django.urls import path
from .views import LandingView, LoginView
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('login', LoginView.as_view(), name='login'),
]
