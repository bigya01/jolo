from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from shop.models import Shop, Service, Client, Appointment
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/auth/login/')
def dashboard_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = get_object_or_404(User, id = request.user.id) 
    return render(request, 'home/index.html', {'shop': shop, 'services': services, 'owner': owner})

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
