from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login/')
def dashboard_view(request, shop_slug):
    
    return render(request, 'home/index.html', {'shop_slug': shop_slug})

def location_view(request):
    return render(request, 'home/map.html')


def users_view(request):
    return render(request, 'home/users.html')


def services_view(request):
    pass

def billing_view(request):
    pass

def target_view(request):
    pass
