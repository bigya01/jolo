from django.shortcuts import render, get_object_or_404
from shop.models import Shop, Service

def shop_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    services = Service.objects.all().filter(shop_id=shop.id)
    return render(request, 'website/shop.html', {'shop': shop, 'services': services})

def user_register(request, shop_slug, service_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    service = get_object_or_404(Service, slug=service_slug)
#TODO
    pass 
