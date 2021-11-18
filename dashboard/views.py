from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import newstats
from django.db.models import Count
from accounts.models import NewUser
from codepartner.models import Session
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

        user_count = NewUser.objects.all().count()
        active_user = NewUser.objects.filter(is_active=True).count()
        blocked_users = NewUser.objects.filter(is_active=False).count()
        sessions = Session.objects.all().count()

        python = Session.objects.filter(language='Python').count()
        js = Session.objects.filter(language='Javascript').count()
        c = Session.objects.filter(language='C').count()
        csharp = Session.objects.filter(language='C#').count()
        cpp = Session.objects.filter(language='C++').count()
        java = Session.objects.filter(language='Java').count()
        php = Session.objects.filter(language='PHP').count()
        r = Session.objects.filter(language='R').count()
        ruby = Session.objects.filter(language='Ruby').count()
        go = Session.objects.filter(language='Go').count()
        other = Session.objects.filter(language='Other').count()
        return render(
            request, 'admin_panel/dashboard.html', {
                'windows': windows, 'mac': mac, 'iphone': iphone, 'android': android, 'others': others, 'total_users': user_count, 'active': active_user, 'blocked': blocked_users, 'sessions': sessions, 'python': python, 'js': js, 'c': c, 'java': java, 'csharp': csharp, 'cpp': cpp, 'php': php, 'r': r, 'ruby': ruby, 'go': go, 'other': other}
        )
