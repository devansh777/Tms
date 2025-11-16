from django.shortcuts import render

def users(request):
    return render(request,'users.html')

def userDashboard(request):
    return render(request,'userDashboard.html')
# Create your views here.
