from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
# Create your views here.


class DashboardView(TemplateView):
    template_name = 'admin/dashboard.html'
