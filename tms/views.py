from django.shortcuts import render
from tms_users.models import TmsUsers

def home(request):
    userCount = TmsUsers.objects.count()
    context = {
        'user_count':userCount
    }
    return render(request,'home.html',context)