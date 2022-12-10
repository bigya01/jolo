from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login/')
def dashboard_view(request):
    return render(request, 'home/index.html')

def location_view(request):
    pass

def users_view(request):
    pass

def services_view(request):
    pass

def billing_view(request):
    pass
