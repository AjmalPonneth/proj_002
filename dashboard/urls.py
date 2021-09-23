from django.urls import path
from .views import DashboardMainView

urlpatterns = [
    path('', DashboardMainView.as_view(), name='dashboard')
]
