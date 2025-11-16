from django.shortcuts import render,redirect
from tms_users.models import TmsUsers

def home(request):
    userCount = TmsUsers.objects.count()
    context = {
        'user_count':userCount
    }
    return render(request,'home.html',context)

def login(request):
    return render(request,'login.html')

def loginAuth(request):
    email = request.POST['email']
    user = TmsUsers.objects.filter(email_id = email)
    if user.count():
        return redirect('userDashboard')
    return redirect('home')