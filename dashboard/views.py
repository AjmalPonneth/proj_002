from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import newstats
from django.db.models import Count
# Create your views here.


class DashboardMainView(View):
    def get(self, request, *args, **kwargs):
        q = newstats.objects.annotate().values('win', 'mac', 'iph', 'android', 'oth')
        new_dic = {}
        for i in q:
            new_dic = i
        windows = new_dic['win']
        mac = new_dic['mac']
        iphone = new_dic['iph']
        android = new_dic['android']
        others = new_dic['oth']
        return render(request, 'admin_panel/dashboard.html', {'windows': windows, 'mac': mac, 'iphone': iphone, 'android': android, 'others': others})
