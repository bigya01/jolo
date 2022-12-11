from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Shop, Service, Client
from shop.forms import ClientRegisterForm, AppointmentRegisterForm

def shop_view(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    services = Service.objects.all().filter(shop_id=shop.id)
    return render(request, 'website/shop.html', {'shop': shop, 'services': services})

def client_register(request, shop_slug, service_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    service = get_object_or_404(Service, slug=service_slug)


    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            response = form.save()
            # return render(request, 'website/appointment_register.html', {'shop': shop, 'services': service, 'form': form})
            user_id = response.id
            return redirect(f"/{shop_slug}/{service_slug}/{user_id}/appointment/register/")
    else:
        form = ClientRegisterForm()   
        return render(request, 'website/client_register.html', {'shop': shop, 'services': service, 'form': form})





def appointment_register(request, shop_slug, service_slug, client_id):
    shop = get_object_or_404(Shop, slug=shop_slug)
    service = get_object_or_404(Service, slug=service_slug)
    if not Client.objects.filter(id=client_id).exists():
        return redirect(f"{shop_slug}/{service_slug}/client/register")
       
    # return render(request, 'website/appointment_register.html', {'shop': shop, 'services': service, 'client_id': client_id})

    if request.method == 'POST':
        form = AppointmentRegisterForm(request.POST)
        if form.is_valid():          
            response = form.save(shop_slug=shop_slug, service_slug=service_slug,client_id = client_id)
            return render(request, 'website/appointment_register_complete.html', {'status': response.appointment_status})
    else:
        form = AppointmentRegisterForm()
        return render(request, 'website/appointment_register.html', {'shop': shop, 'services': service, 'form': form, 'client_id': client_id})