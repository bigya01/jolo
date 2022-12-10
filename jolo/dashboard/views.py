from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from shop.models import Shop, Service, Client, Appointment
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/auth/login/')
def dashboard_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)

    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)
    
    return render(request, 'home/index.html', {'shop': shop, 'services': services, 'owner': owner})



@login_required(login_url='/auth/login/')
def location_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    
    return render(request, 'home/map.html')

@login_required(login_url='/auth/login/')
def users_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)
    
    return render(request, 'home/users.html')

@login_required(login_url='/auth/login/')
def services_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)
    
    # TODO: render template
    pass

@login_required(login_url='/auth/login/')
def billing_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)

    # TODO: render template
    pass

@login_required(login_url='/auth/login/')
def target_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)

    # TODO: render template
    pass
