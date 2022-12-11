from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from shop.models import Shop, Service, Client, Appointment
from django.contrib.auth.models import User
from django.http import  HttpResponse


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
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)
    return render(request, 'home/map.html', {'shop': shop, 'services': services, 'owner': owner})

@login_required(login_url='/auth/login/')
def users_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)
    
    return render(request, 'home/users.html', {'shop': shop, 'services': services, 'owner': owner})

@login_required(login_url='/auth/login/')
def marketing_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)

    APP_DOMAIN = "http://127.0.0.1:8000"
    SHOP_SLUG = shop_slug
    SHOP_URL = f"{APP_DOMAIN}/{SHOP_SLUG}"
    facebook_share_url = f"https://www.facebook.com/dialog/share?app_id=87741124305&href={SHOP_URL}"
    twitter_share_url = f"https://twitter.com/intent/tweet?url={SHOP_URL}"
    whatsapp_share_url = f"https://api.whatsapp.com/send/?text={SHOP_URL}-s&type=custom_url&app_absent=0"
    reddit_share_url = f"https://www.reddit.com/submit?url={SHOP_URL}"  

   
    return render(request, 'home/marketing.html', {'shop': shop, 'services': services, 'owner': owner, "facebook_share_url": facebook_share_url, "twitter_share_url": twitter_share_url, "whatsapp_share_url": whatsapp_share_url, "reddit_share_url": reddit_share_url})


@login_required(login_url='/auth/login/')
def services_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)
    # random ratings
    ratings = range(100)
    
    
    
    return render(request, 'home/services.html', {'shop': shop, 'services': services, 'owner': owner, "ratings": ratings})

@login_required(login_url='/auth/login/')
def billing_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)

    # TODO: render template DO NOT FORGET TO PASS DICTIONARY=> {'shop': shop, 'services': services, 'owner': owner}
    pass

@login_required(login_url='/auth/login/')
def target_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    if not request.user.id == shop.user_id:
        return HttpResponse("You are not authorized to view this page!")
    services = Service.objects.all().filter(shop_id=shop.id)
    owner = User.objects.get(id = request.user.id)

    # TODO: render template DO NOT FORGET TO PASS DICTIONARY=> {'shop': shop, 'services': services, 'owner': owner}
    pass
